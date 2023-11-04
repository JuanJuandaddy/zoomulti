# -*-coding:utf-8-*-
# -*-this is a python script -*-
# -*-20230615-*-




#json消息分隔符
MsgBarrier='/'

#IP地址 Server的地址
IP='192.168.10.3'
#IP='127.0.0.1'


#监听端口
PORT=8888

#队列长度
QUEUE_LEN=500

#控制器数量
CONTROLLER_NUM=5

#Socket
SERVER_RECV_BUFSIZE=204800000 #服务器接受控制器的soocket接受缓冲区大小，如果过小会导致json解析消息错误,单位字节
#2048000即2000KB≈2MB
CLIENT_RECV_BUFSIZE=204800000 #控制器接受服务器的socket接受缓冲区的大小，单位字节
#角色对象

# 控制器角色代码
# OFPCR_ROLE_NOCHANGE = 0, /* 不改变当前角色. */
# OFPCR_ROLE_EQUAL = 1, /* 默认角色，完全读写. 一个ovs可以有多个equal*/
# OFPCR_ROLE_MASTER = 2, /* 完全读写，但是只能有一个master，一旦设置为master，其他所连接的控制器都为slave */
# OFPCR_ROLE_SLAVE = 3, /* 只具有只读权限，而且异步消息不能获取，只能获取Port-Status消息*/

ID_ROLE_MAP={
    0:"NOCHANGE",
    1:"EQUAL",
    2:"MASTER",
    3:"SLAVE"
}

#Controller
ECHO=5#单位秒

CONTROLLER_IP='127.0.0.1' #控制器的IP

OFP_VERSION='OpenFlow13'#openflow版本

ECHO_DELAY=1#几个周期后开始request

PKT_IN_ECHO=5 #打印packet_in消息的间隔

HANDLE_DELAY_ECHO=5 #打印交换机平均响应时延的间隔

SW_TO_SW_PRIORITY=30 #交换机之间的流表传输优先级

IPV6_PRIORITY=65534#IPV6表项的优先级

SW_TO_HOST_PRIORITY=50#接入层流表的优先级

TABLEMISS_PRIORITY=0#table-miss的优先级

CROSSREQUIRE_PRIORITY=30#跨域请求的流表优先级

IDLE_TIME_OUT=0 #空闲过期时间  跨域与非跨域过期时间相同

HARD_TIME_OUT=0 #绝对过期时间  跨域与非跨域过期时间相同

#Server
WAIT_CONNECT=10   #最大等待连接数

MONITOR=10        #打印消息周期

#TOPO
CONTROLLERS=['c0','c1','c2','c3','c4']#控制器ID，代表有子网0和子网1，代表着有area0和area1两个控制area，
                            # 在Ryu源码中该配置极其重要，务必2者保持一致

CONTROLLER_PORTS=[6653,6654,6655,6656,6657] #控制器端口

WAITING_FOR_STABLE_NETWORK_SECONDS=10

#链路连接信息，端口可以不指定，如果需要指定链接的端口，前往os3e拓扑文件中的create——link方法中，使用port信息
EDGE_LINK={("s13","s33"):[3,2],("s15","s31"):[5,2],("s16","s21"):[4,2]
           ,("s22","s31"):[2,4],("s23","s32"):[2,2],("s24","s51"):[3,2],
           ("s26","s55"):[3,2],("s33","s43"):[3,2],("s34","s52"):[3,2],
           ("s54","s40"):[3,2]}#边缘交换机的连接端口，用于Server对全局拓扑的初始化

SW_LINK={("s10","s11"):[2,2],("s10","s13"):[5,2],("s10","s15"):[4,2],("s10","s12"):[3,2],
        ("s12","s14"):[3,2],("s14","s15"):[3,3],("s14","s16"):[4,2],("s16","s15"):[3,4],
        ("s21","s20"):[3,2],("s20","s22"):[3,3],("s31","s32"):[3,3],("s20","s25"):[4,2],
        ("s23","s25"):[3,3],("s32","s30"):[4,3],("s30","s33"):[2,4],("s25","s24"):[4,2],
        ("s25","s26"):[5,2],("s30","s34"):[4,2],("s52","s53"):[3,2],("s51","s53"):[3,3],
        ("s53","s50"):[4,2],("s50","s55"):[4,3],("s55","s56"):[4,2],("s50","s54"):[3,2],
        ("s40","s41"):[3,2],("s41","s42"):[3,2],("s42","s43"):[3,3],("s43","s44"):[4,2],
        ("s44","s45"):[3,2],("s45","s46"):[3,2],("s46","s47"):[3,2],("s47","s40"):[3,4]}
        #交换机之间的链路

#get map
def get_map(LINKS):
    PREPARE=["s"+str(i) for i in range(10,60)]
    ALL=PREPARE.copy()
    for k in LINKS.keys():

        if k[0] in PREPARE:
            PREPARE.remove(k[0])
        if k[1] in PREPARE:
            PREPARE.remove(k[1])
    for h in PREPARE:
        ALL.remove(h)

    HOSTS = {}
    SW_LIST = [[] for _ in range(5)]
    HOST_LIST = [[] for _ in range(5)]

    def h(x):
        return x, "h" + x.split("s")[1]

    for host in map(h, ALL):
        HOSTS[host[0]] = host[1]


    for c in ALL:
        SW_LIST[int(list(c)[1])-1].append(c)
        HOST_LIST[int(list(c)[1])-1].append("h"+c.split("s")[1])

    return HOSTS,SW_LIST,HOST_LIST

SW_HOST,SWS,HOSTS=get_map(SW_LINK)
# SW_HOST 交换机与主机之间的映射
# SWS  全体交换机，区分控制器
# HOSTS 全体主机，区分控制器

#MAC
UNKNOWN_MAC='00:00:00:00:00:00'#ARP请求的IP中默认的未知MAC

BROADCAST_MAC='ff:ff:ff:ff:ff:ff' #广播地址

#PingAll Parameters 默认采取PING  非HPING3

PING_NUM=5 #每个主机发送 x 个ping包来实现基础网络互通

PING_INTERVAL=0.01 #每对主机之间的间隔时间 单位秒

PING_OUT_MODE=0 #是否域外ping ，1 is 开 || 0 is 不开

PING_IN_OUT_INTERVAL=3 #开启域外ping之后，此选项才有效。域内和域外ping的时间间隔 单位秒

#Packet_In Parameters  默认采取HPING3  非PING
BLACKHOLE_PKTIN_IP_STYLE='192.168' #黑洞地址的前半缀

BLACKHOLE_PKTIN_IP_SUBNET=['1']  #黑洞地址的子网分地址  255.255.0.0，不可与网络中的任何子网地址相同

GENERATE_MODE=0 #产生pktin的模式，0 is gevent单线程 || 1 is asyncio单线程  || 2 is asyncio多线程

SPEED_MODE=0 #pktin速度模式，0 is 随机模式，模拟正常packet-in || 1 is 压力测试

