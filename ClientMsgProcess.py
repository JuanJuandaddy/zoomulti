"""
Server唯一外部处理类
服务器对于每个控制器的处理方法,
"""
import json
from functools import reduce
import networkx as nx
from StreamInfo import InfoProcess
from gevent import monkey;monkey.patch_all()
from gevent import spawn
import settings
class ClientMsgProcess(object):
    def __init__(self,client):
        self.client=client
        self.log=InfoProcess()

    def process(self,msg):
        func_name = msg["msg_type"]
        func_map = {
            "sw_register": "_sw_register",
            "get_topo": "_get_topo",
            "shortest_path": "_shortest_path",
            "register_acc_info": "_register_acc_info",
            "packet_out": "_packet_out",
            "arp_cross_ip": "_arp_cross_ip",
            "register_arp_table": "_register_arp_table",
            "pktin_load": "_pktin_load"
        }
        # 根据函数关系映射
        if func_name in func_map:
            actual_func_name = func_map[func_name]
            if hasattr(self, actual_func_name) and callable(getattr(self, actual_func_name)):
                function_to_call = getattr(self, actual_func_name)
                spawn(function_to_call,msg)
            else:
                print(f"{actual_func_name} 不是可调用函数")
        else:
            print("功能函数未开发:", func_name)
    """
       消息入口类
    """
    def _sw_register(self,msg):
        gra = self.client.server.graph

        dpid = msg["dpid"]
        master_controller = msg["master_controller"]

        self.client.server.switches[dpid] = master_controller

        controller_to_switches=self.client.server.controller_to_switches

        if master_controller not in controller_to_switches.keys():
            self.client.server.controller_to_switches.setdefault(master_controller,[])
        else:
            self.client.server.controller_to_switches[master_controller].append(dpid)
        if not gra.has_node(dpid):
            gra.add_node(dpid) #给图添加节点

    def _get_topo(self,msg):
        """
            画出每个控制器自己的area拓扑，但是并不能画出边界交换机之间的连接关系，处理该类连接关系的方法在register_edge_sw
        """
        gra=self.client.server.graph

        if msg["topo_type"]=="link_list":
            link=msg["data"]

            src_dpid = link["src_dpid"]
            dst_dpid = link["dst_dpid"]
            src_port = link["src_port"]
            dst_port = link["dst_port"]

            #给图添加边

            gra.add_edge(src_dpid, dst_dpid,src_port=src_port,dst_port=dst_port)

            self.client.server.topo[(src_dpid,dst_dpid)]=(src_port,dst_port)

    def _shortest_path(self,msg):
        """
        处理控制器发出的跨域IP请求，当收到的请求在全域路径表中，返回路径，否则就计算最短路径。返回路径表
        处理返回的路径表，通过交换机从属表判断路径表中各个交换机的从属状况，将路径分为n个域
        比如[1,2,3,4,5] 当4,5属于域2,且1,2,3属于域1中，则将路径表分为2个域，[1,2,3]、[4,5]，随后分别
        将这2个域中的控制器下发消息即可完成


        由于packet_out的时候，一般是接入层交换机先触发packet_in，随后再去计算路径，通过给路径的中间节点
        下发流表，给接入层交换机下发packet_out来让网络互通，正常情况来说中间节点不会再触发packet_in，但是由于流表下发的顺序性质
        在下发接入层的packet_out时，数据包发出到达下一转发节点的ovs的时候，此时中间节点的安装不及时，并没有流表，故也会触发packet_in
        故也需要对此类ovs进行处理，所以创建了dpath来处理该类packet_in

        nx的最短路径算法存在bug，该方法可能导致计算后的路径不包含首节点
        """
        gra=self.client.server.graph
        data=msg["data"]
        ip_src,ip_dst=data["ip_src"],data["ip_dst"]

        key_ip=(ip_src,ip_dst)

        src_dpid,dst_dpid=data["src_dpid"],self.find_dst_area(ip_dst)[0]
        if dst_dpid ==None:
            return
        buffer_id,msg_data,in_port=data["buffer_id"],data["msg_data"],data["in_port"]

        key_dpid=(src_dpid,dst_dpid)
        paths=self.client.server.paths
        dpaths=self.client.server.dpaths
        switches=self.client.server.switches


        """
            下方两种校验用途如下
            即存在一个交换机下存在1个以上的主机
            对于两个不同交换机下不同主机进行通信，采取的路径相同即可不考虑负载均衡的情况
            对此需要收集不同主机之间的路径以及不同交换机之间的路径，方便后续直接拿出
        """

        if key_ip not in paths.keys():
            #不存在于全域IP路径表
            path = nx.shortest_path(gra, src_dpid, dst_dpid)
            #self.log.info(f'src_dpid:{src_dpid} ==> dst_dpid:{dst_dpid} path is :{path}')
            while path[0] != src_dpid:#校验路径表的合法性
                path = nx.shortest_path(gra, src_dpid, dst_dpid)
                if path[0] == src_dpid:
                    break
            paths[key_ip]=path #存储计算后的路径表
            dpaths[key_dpid]=path #存储该dpid路径表


        if key_dpid not in dpaths.keys():
            #不存在全域dpid路径表

            path = nx.shortest_path(gra, src_dpid, dst_dpid)
            #self.log.info(f'src_dpid:{src_dpid} ==> dst_dpid:{dst_dpid} path is :{path}')
            while path[0] != src_dpid:#校验路径表是否正确
                path = nx.shortest_path(gra, src_dpid, dst_dpid)
                if path[0] == src_dpid:
                    break
            dpaths[key_dpid] = path  # 存储计算后dpid路径表

        #以dpaths为主，paths为辅

        p=dpaths[key_dpid]
        #存在于全域路径表
        cid_nodelist_map=self.search_controller_pathnode_map(path=p,switches=switches)
        #self.log.info(f'src:{key_dpid[0]} -> dst:{key_dpid[1]} path:{p} map:{cid_nodelist_map}')
        """
            cid_nodelist_map:
            假设switches的映射为：{1:1,2:1,3:1,4:2,5:2,6:2,7:3,8:3}
            假设path为[1,2,4,5,7,8]
            cid_nodelist_map is :{1: 2, 2: 2, 3: 2}
            
        """
        self.build_packetout(controller_id=int(switches[p[0]]-1),data=msg_data,f=p[0],s=p[1],buffer_id=buffer_id,in_port=in_port)

        """
            首先需要对首节点与次节点进行packet_out,再进行中间节点的流表下发
        """
        self.distribute_flowmod(gra,key_ip,cid_nodelist_map,p)

        """
            依次让map中存在的控制器进行下发相关流表命令
            self.client.server.controller_obj  {controller_id:该controller的socket句柄} 
        """

    def _register_acc_info(self,msg):
        """
        ovs与IP之间的映射唯一，不需要做判断处理
        :param msg: 消息体
        :return: 注册ovs与IP的映射
        """
        data=msg["data"]
        dpid,in_port,ip,area_id=data["dpid"],data["in_port"],data["ip"],data["area_id"]


        key=(dpid,in_port)

        if key not in self.client.server.sw_ip.keys():
            self.client.server.sw_ip.setdefault(key,{})


        self.client.server.sw_ip[key]["ip"] = ip
        self.client.server.sw_ip[key]["area_id"] = area_id

    def _arp_cross_ip(self,msg):
        """
        :param msg: arp的跨域请求
        :return:
        """
        data=msg["data"]
        dpid,in_port,src_ip,dst_ip,msg_data=data["dpid"],data["in_port"],data["src_ip"],data["dst_ip"],data["msg_data"]

        #源area
        src_area=self.client.server.switches[dpid]


        #目的area,如果已经存储了ip与dpid的映射关系，则根据dst_ip找到目的area,否则向除了src_area的其他area发送FLOOD
        #同时可以更新ip与dpid的映射关系


        # 返回目的IP的areaID也等同于目的dp的master控制器、目的交换机、IP与交换机连接的端口
        dst_dpid,port,dst_area,flag=self.find_dst_area(dst_ip)


        if flag:
            #当找到目的IP的相关信息
            self.build_packetout(controller_id=dst_area,data=msg_data,f=dst_dpid,out_port=port)#下发packet_out
        else:
            #未找到目的IP的相关信息，说明Server也没有存储，进行FLOOD，找到目的IP的相关信息，向除了src_area的其他area下发FLOOD
            # 若查找目的IP已向某控制器下发过FLOOD，则忽略
            if dst_ip not in self.client.server.FLOOD_IP:
                msg=json.dumps({
                    "msg_type":"flood",
                    "data":{
                        "msg_data":msg_data
                    }
                })

                area_dict=self.client.server.switches.copy()
                area_list=list(set(area_dict.values()))
                area_list.remove(src_area)

                def sub_one(x):
                    return x-1

                for controller in map(sub_one,area_list):
                    self.hook_handler(controller_id=controller,msg=msg)

                self.client.server.FLOOD_IP.append(dst_ip)

    def _packet_out(self,msg):
        """
            由Server代理发送packetout，用于处理跨域ARP请求
        """
        data=msg["data"]
        dst_ip,msg_data=data["dst_ip"],data["msg_data"]

        dst_dpid, port, dst_area, flag = self.find_dst_area(dst_ip)

        if flag:
            self.build_packetout(controller_id=dst_area, data=msg_data, f=dst_dpid, out_port=port)
        else:
            self.log.info(f'代理发送packetout失败：dst_dpid:{dst_dpid} port:{port} dst_area:{dst_area}')

    def _register_arp_table(self,msg):

        #注册IP:MAC
        data=msg["data"]
        ip,mac=data["ip"],data["mac"]

        self.client.server.arp_table[ip]=mac

    def _pktin_load(self,msg):
        #pktin负载处理方法
        data=msg["data"]

        sw_pktin={}

        controller_id,controller_pktin,controller_delay,switches_pktin=data["controller_id"],data["controller_pktin"],data["controller_delay"],data["switches_pktin"]

        if controller_id not in self.client.server.controller_pktin_load.keys():

            #首次注册

            self.client.server.controller_pktin_load.setdefault(controller_id,{})# 初始化

            self.client.server.controller_pktin_load[controller_id]["pktin"]=controller_pktin

            self.client.server.controller_pktin_load[controller_id]["delay"] = controller_delay

            for dp_dpsp in switches_pktin:

                sw_pktin.setdefault(dp_dpsp[0],{})

            self.client.server.switches_pktin_load.setdefault(controller_id, sw_pktin)  # 初始化

            for dp_dpsp in switches_pktin:

                self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["pktin_speed"]=dp_dpsp[1]

                self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["pktin_size"] = dp_dpsp[2]

                if controller_pktin!=0:

                    self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["percentage"] = f'{(dp_dpsp[1] / controller_pktin)*100:.4f}%'

                else:

                    self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["percentage"] =  f'0%'

        else:

            #后续更新

            self.client.server.controller_pktin_load[controller_id]["pktin"] = controller_pktin

            self.client.server.controller_pktin_load[controller_id]["delay"] = controller_delay

            for dp_dpsp in switches_pktin:

                self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["pktin_speed"] = dp_dpsp[1]

                self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["pktin_size"] = dp_dpsp[2]

                if controller_pktin != 0:

                    self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["percentage"] = f'{(dp_dpsp[1] / controller_pktin)*100:.4f}%'

                else:

                    self.client.server.switches_pktin_load[controller_id][dp_dpsp[0]]["percentage"] = f'0%'

    """
        消息处理类
    """

    @staticmethod
    def search_controller_pathnode_map(path,switches):
        """
        :param path: 路径表
        :param switches: 交换机与其控制的主控制器之间的map映射
        """
        s = []
        res = {}
        #path=path[:-1]
        for id in path:
            if id in switches.keys():
                s.append(switches[id])
        #去重
        f = lambda x, y: x if y in x else x + [y]
        s = reduce(f, [[], ] + s)
        for cid in s:
            res[cid] = []
        for node in path:
            for sw, con in switches.items():
                if sw == node:
                    res[con].append(node)  #{controller_id: [pathnode,pathnode]....}
        for k, v in res.items():
            res[k] = len(v)

        return res

    def build_packetout(self,controller_id,data,f=None,s=None,out_port=None,buffer_id=None,in_port=None):
        if f and s:
            #处理IP packetout
            gra = self.client.server.graph
            out_port=gra[f][s]["src_port"]

        else:
            #处理ARP packetout
            out_port=out_port

        msg=json.dumps({
            "msg_type":"packet_out",
            "data":{
                "dpid":f,
                "out_port":out_port,
                "msg_data":data,
                "buffer_id":buffer_id,
                "in_port":in_port
            }
        })
        self.hook_handler(controller_id,msg)

    def distribute_flowmod(self,gra,key_ip,cid_nodelist_map,path):
        g_index=0 #全局索引
        for cid,t in cid_nodelist_map.items():

            t+=g_index

            for index in range(g_index,t):
                if index<len(path)-1:#处理头节点以及中间节点

                    out_port=gra[path[index]][path[index+1]]["src_port"]
                    dpid=path[index]
                    self.send_flow_mod(cid-1,dpid,key_ip,out_port)#调用cid的句柄，发送流表下发命令

            g_index=t

    def send_flow_mod(self,controller_id,dpid,key_ip,out_port):
        """
        :param controller_id: 控制器对象
        :param dpid: ovsID
        :param key_ip: （ipsrc,ipdst）
        :param out_port: dpid匹配到该key_ip的出端口
        """
        msg=json.dumps({
            "msg_type":"flow_mod",
            "data":{
                "dpid": dpid,
                "ip_src": key_ip[0],
                "ip_dst":key_ip[1],
                "out_port":out_port
            }
        })
        self.hook_handler(controller_id,msg)

    def hook_handler(self,controller_id,msg):
        """
        :param controller_id: controller的ID
        :param msg: 消息体
        :return: 发送给指定controller的消息
        """
        # 调用controller_id的发送消息句柄
        self.client.server.controller_obj[controller_id].send_to_queue(msg)

    def get_controller_id(self,dpid):
        return self.client.server.switches[dpid]

    def find_dst_area(self,dst_ip):
        for key, value in self.client.server.sw_ip.items():
            if dst_ip == value["ip"]:
                # 找到了目的IP的area_id
                return key[0], key[1], int(value["area_id"]), True
        return None, None, None, False





