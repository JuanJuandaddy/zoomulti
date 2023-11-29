#-*-集群部署初始配置文件-*-
MsgBarrier='/'
PORT=8888
IP='192.168.10.3'
#IP='127.0.0.1'
QUEUE_LEN=500
CONTROLLER_NUM=5
SERVER_RECV_BUFSIZE=204800000
CLIENT_RECV_BUFSIZE=204800000
ID_ROLE_MAP={0: 'NOCHANGE', 1: 'EQUAL', 2: 'MASTER', 3: 'SLAVE'}
ECHO=5
CONTROLLER_IP='127.0.0.1'
OFP_VERSION='OpenFlow13'
ECHO_DELAY=1
PERFORMANCE_STATISTIC_ECHO=5
SW_TO_SW_PRIORITY=30
IPV6_PRIORITY=65534
SW_TO_HOST_PRIORITY=50
TABLEMISS_PRIORITY=0
CROSSREQUIRE_PRIORITY=30
IDLE_TIME_OUT=0
HARD_TIME_OUT=0
WAIT_CONNECT=10
WAITING_FOR_STABLE_NETWORK_SECONDS=10
# CONTROLLERS=['c0','c1']
# CONTROLLER_PORTS=[6653,6654]
# EDGE_LINK={('s2','s3'):[2,2]}
# SW_LINK={('s1','s2'):[1,1],('s3','s4'):[1,1]}
# SW_HOST={'s1':['h1'],'s2':['h2'],'s3':['h3'],'s4':['h4']}
# SWS=[['s1','s2'],['s3','s4']]
# HOSTS=[[['h1'],['h2']],[['h3'],['h4']]]
CONTROLLERS=['c0', 'c1', 'c2', 'c3', 'c4']
CONTROLLER_PORTS=[6653, 6654, 6655, 6656, 6657]
EDGE_LINK={('s13', 's33'): [3, 2], ('s15', 's31'): [5, 2], ('s16', 's21'): [4, 2], ('s22', 's31'): [2, 4], ('s23', 's32'): [2, 2], ('s24', 's51'): [3, 2], ('s26', 's55'): [3, 2], ('s33', 's43'): [3, 2], ('s34', 's52'): [3, 2], ('s54', 's40'): [3, 2]}
SW_LINK={('s10', 's11'): [2, 2], ('s10', 's13'): [5, 2], ('s10', 's15'): [4, 2], ('s10', 's12'): [3, 2], ('s12', 's14'): [3, 2], ('s14', 's15'): [3, 3], ('s14', 's16'): [4, 2], ('s16', 's15'): [3, 4], ('s21', 's20'): [3, 2], ('s20', 's22'): [3, 3], ('s31', 's32'): [3, 3], ('s20', 's25'): [4, 2], ('s23', 's25'): [3, 3],
         ('s32', 's30'): [4, 3], ('s30', 's33'): [2, 4], ('s25', 's24'): [4, 2], ('s25', 's26'): [5, 2], ('s30', 's34'): [4, 2], ('s52', 's53'): [3, 2], ('s51', 's53'): [3, 3], ('s53', 's50'): [4, 2], ('s50', 's55'): [4, 3], ('s55', 's56'): [4, 2], ('s50', 's54'): [3, 2], ('s40', 's41'): [3, 2], ('s41', 's42'): [3, 2],
         ('s42', 's43'): [3, 3], ('s43', 's44'): [4, 2], ('s44', 's45'): [3, 2], ('s45', 's46'): [3, 2], ('s46', 's47'): [3, 2], ('s47', 's40'): [3, 4]}
SW_HOST={'s10': ['h1001', 'h1002', 'h1003'], 's11': ['h1101', 'h1102', 'h1103'], 's12': ['h1201', 'h1202', 'h1203'], 's13': ['h1301', 'h1302', 'h1303'], 's14': ['h1401', 'h1402', 'h1403'], 's15': ['h1501', 'h1502', 'h1503'], 's16': ['h1601', 'h1602', 'h1603'],
         's20': ['h2001', 'h2002', 'h2003'], 's21': ['h2101', 'h2102', 'h2103'], 's22': ['h2201', 'h2202', 'h2203'], 's23': ['h2301', 'h2302', 'h2303'], 's24': ['h2401', 'h2402', 'h2403'], 's25': ['h2501', 'h2502', 'h2503'], 's26': ['h2601', 'h2602', 'h2603'],
         's30': ['h3001', 'h3002', 'h3003'], 's31': ['h3101', 'h3102', 'h3103'], 's32': ['h3201', 'h3202', 'h3203'], 's33': ['h3301', 'h3302', 'h3303'], 's34': ['h3401', 'h3402', 'h3403'],
         's40': ['h4001', 'h4002', 'h4003'], 's41': ['h4101', 'h4102', 'h4103'], 's42': ['h4201', 'h4202', 'h4203'], 's43': ['h4301', 'h4302', 'h4303'], 's44': ['h4401', 'h4402', 'h4403'], 's45': ['h4501', 'h4502', 'h4503'], 's46': ['h4601', 'h4602', 'h4603'], 's47': ['h4701', 'h4702', 'h4703'],
         's50': ['h5001', 'h5002', 'h5003'], 's51': ['h5101', 'h5102', 'h5103'], 's52': ['h5201', 'h5202', 'h5203'], 's53': ['h5301', 'h5302', 'h5303'], 's54': ['h5401', 'h5402', 'h5403'], 's55': ['h5501', 'h5502', 'h5503'], 's56': ['h5601', 'h5602', 'h5603']}
SWS=[['s10', 's11', 's12', 's13', 's14', 's15', 's16'],
     ['s20', 's21', 's22', 's23', 's24', 's25', 's26'],
     ['s30', 's31', 's32', 's33', 's34'],
     ['s40', 's41', 's42', 's43', 's44', 's45', 's46', 's47'],
     ['s50', 's51', 's52', 's53', 's54', 's55', 's56']]
HOSTS=[[['h1001', 'h1002', 'h1003'], ['h1101', 'h1102', 'h1103'], ['h1201', 'h1202', 'h1203'], ['h1301', 'h1302', 'h1303'], ['h1401', 'h1402', 'h1403'], ['h1501', 'h1502', 'h1503'], ['h1601', 'h1602', 'h1603']],
       [['h2001', 'h2002', 'h2003'], ['h2101', 'h2102', 'h2103'], ['h2201', 'h2202', 'h2203'], ['h2301', 'h2302', 'h2303'], ['h2401', 'h2402', 'h2403'], ['h2501', 'h2502', 'h2503'], ['h2601', 'h2602', 'h2603']],
       [['h3001', 'h3002', 'h3003'], ['h3101', 'h3102', 'h3103'], ['h3201', 'h3202', 'h3203'], ['h3301', 'h3302', 'h3303'], ['h3401', 'h3402', 'h3403']],
       [['h4001', 'h4002', 'h4003'], ['h4101', 'h4102', 'h4103'], ['h4201', 'h4202', 'h4203'], ['h4301', 'h4302', 'h4303'], ['h4401', 'h4402', 'h4403'], ['h4501', 'h4502', 'h4503'], ['h4601', 'h4602', 'h4603'], ['h4701', 'h4702', 'h4703']],
       [['h5001', 'h5002', 'h5003'], ['h5101', 'h5102', 'h5103'], ['h5201', 'h5202', 'h5203'], ['h5301', 'h5302', 'h5303'], ['h5401', 'h5402', 'h5403'], ['h5501', 'h5502', 'h5503'], ['h5601', 'h5602', 'h5603']]]
ADJACENCY_CONTROLLER={
    "c1":["c2","c3"],
    "c3":["c1","c2","c4","c5"],
    "c2":["c1","c5","c3"],
    "c4":["c3","c5"],
    "c5":["c2","c3","c4"]
}
CONTROLLERS_EDGE_SWITCHES_AREA={
    "c1":{("s13",3):2,("s15",5):2,("s16",4):1},
    "c2":{("s22",2):2,("s21",2):0,("s23",2):2,("s24",3):4,("s26",3):4},
    "c3":{("s31",2):0,("s31",4):1,("s32",2):1,("s33",2):0,("s33",3):3,("s34",3):4},
    "c4":{("s43",2):2,("s40",2):4},
    "c5":{("s51",2):1,("s52",2):2,("s54",3):3,("s55",2):1}
}
CONTROLLER_EDGE_SWITCHES={
    "c1":["s13","s15","s16"],
    "c2":["s22","s21","s23","s24","s26"],
    "c3":["s31","s32","s33","s34"],
    "c4":["s43","s40"],
    "c5":["s51","s52","s54","s55"]
}
IF_ARP=True
PING_NUM=5
PING_INTERVAL=0.5
PING_OUT_MODE=0
PING_IN_OUT_INTERVAL=3
UNKNOWN_MAC='00:00:00:00:00:00'
BROADCAST_MAC='ff:ff:ff:ff:ff:ff'
CONTROLLER_PKT_THRESHOLD=1600
EACH_SW_HOSTS_NUM=3
SAVE_DATA_PERIOD=10