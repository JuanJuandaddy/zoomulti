# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
plt.rcParams['font.sans-serif']='SimHei'
import numpy as np
# plt.figure(figsize = (15,10), dpi = 100)
# c1=[9.4,10.2,10.0,9.8,9.4,9.4,158.8,698.6,656.8,674.4,649.0,1079.2,1151.0,1825.8,1945.6,1791.2,1586.6,1817.0,1817.2,1740.4,1740.0,1561.2,1458.8,1715.0,1714.6,1663.6,1612.0,1765.8,1612.2,1586.4]
# c2=[9.8,9.2,8.8,8.6,8.8,776.4,708.2,670.4,627.0,621.8,625.6,582.4,560.8,522.8,541.8,518.0,519.8,507.8,553.0,493.0,447.2,468.0,472.0,500.0,481.4,499.8,491.6,511.8,470.4,484.8]
# c3=[8.6,8.0,8.6,8.8,8.0,762.4,717.0,643.0,671.2,685.8,697.8,663.6,600.2,537.2,561.2,527.8,547.6,592.2,570.6,527.0,492.8,492.6,490.0,506.4,481.4,505.4,505.0,499.2,504.8,508.6]
# c4=[8.6,8.0,8.8,9.0,8.6,8.8,689.0,645.6,669.6,692.0,656.6,595.8,596.6,559.6,590.8,540.8,424.6,565.0,514.4,524.0,520.0,490.8,496.4,493.0,552.4,456.0,504.8,557.4,494.6,539.2]
# c5=[8.2,8.2,9.2,8.4,8.0,219.8,687.0,639.2,663.6,675.0,650.4,608.4,627.2,587.0,514.4,563.4,456.6,569.0,533.6,523.6,503.2,461.8,449.2,516.8,552.4,485.8,492.8,519.0,541.0,530.6]
# x= [i for i in range(1,31)]
# plt.plot(x,c1, c = 'red',label="c1",marker='v',markersize=16,linewidth=2.0,linestyle='--')
# plt.plot(x,c2, c = 'blue',label="c2",marker='*',markersize=16,linewidth=2.0,linestyle='--')
# plt.plot(x,c3, c = 'green',label="c3",marker='>',markersize=16,linewidth=2.0,linestyle='--')
# plt.plot(x,c4, c = 'yellow',label="c4",marker='o',markersize=16,linewidth=2.0,linestyle='--')
# plt.plot(x,c5, c = 'pink',label="c5",marker='d',markersize=16,linewidth=2.0,linestyle='--')
# plt.xticks([i for i in range(0,35,5)],fontsize=20)
# plt.yticks([i for i in range(0,2000,200)],fontsize=20)
# plt.xlabel("第几个周期/10s", fontdict = { 'size' : 24 })
# plt.ylabel("控制器负载PacketIn/s", fontdict = { 'size' : 24 })
# plt.legend(fontsize=30)
# plt.show()
#==============时延曲线
# plt.rcParams['font.sans-serif']='SimHei'
# import numpy as np
# plt.figure(figsize = (15, 10), dpi = 100)
# y=[0.08,0.17,0.24,0.61,0.7,0.97,3.40]
# x= [100,400,700,1000,1300,1600,1900]
# plt.plot(x,y, c = 'red',label="时延曲线",marker='v',markersize=16,linewidth=2.0,linestyle='--')
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel("PacketIn速率", fontdict = { 'size' : 24 })
# plt.ylabel("控制器处理单个PacketIn平均延迟/ms", fontdict = { 'size' : 24 })
# plt.legend(fontsize=20)
# plt.show()
#==============对比曲线
#static策略
static_load=[8.2,8.8,28.6,1527.4,1540.4,1875.8,1848.8,1972.8,1897.4,1877.8,1788.0,1783.2,1884.8,
	1694.6,1918.4,1889.1]
static_rate=[0.4384,0.3104,1779.1776,259717.3856,276183.7184,
	408997.9584,392105.072,455611.1296,414458.0736,411429.0816,
	369274.5056,367834.0896,413922.5504,333516.7584,432326.2144,
	 417176.4680]

#
# #csm:
csm_load=[8.0,9.0, 1847.6,1362.8, 1487.4,1650.6,1048.0,1086.6 ,
	908.8,1228.0,1258.4,1232.2,1165.2,1237.4,1071.0,1241.4]
csm_rate=[0.4896,0.24,416461.7024,204005.248,242659.712,300202.5856,99455.7184,108483.0976,
	 78654.848 ,141156.3936,146350.2144,139539.152,124257.8464,144707.7184,107738.7616,143888.1831]
#
# #vikor:
vikor_load=[8.8, 8.4 ,1528.0 ,1774.4,495.4,499.4,492.2,475.6,485.8 ,473.4,
	478.6,476.2,468.0,441.0,469.6,444.6,]
vikor_rate=[0.112 , 0.2016 ,274338.3584,109949.936,386702.1664 ,110875.584 ,100648.7264 ,100046.3264 ,98623.28,
	102610.2464,102717.2896,93198.3104,83076.6624,93316.816,81619.7856,101993.936]
#
# #lsm:
lsm_load=[8.2 ,8.4,1526.6 ,1817.8, 1377.0, 1416.4 ,1405.2,1391.8,1418.8,
	1410.2,1366.0,1351.2,1395.0,1398.0,1396.8,1440.2]
lsm_rate=[0.2016 ,0.4896, 276556.7264,407572.6304,200588.5184,213255.7024,207112.5056,204315.0624,
	212438.9024,208802.7936 , 195486.368,193620.2464,204946.6944,205605.3344,205534.0416,220286.352]
plt.figure(figsize = (15,10), dpi = 100)
#16个监控周期
x= [i for i in range(1,17)]
plt.plot(x,vikor_rate, c = 'red',label="vikor",marker='v',markersize=16,linewidth=2.0,linestyle='--')
plt.plot(x,csm_rate, c = 'blue',label="csm",marker='*',markersize=16,linewidth=2.0,linestyle='--')
plt.plot(x,lsm_rate, c = 'green',label="lsm",marker='>',markersize=16,linewidth=2.0,linestyle='--')
plt.plot(x,static_rate, c = 'black',label="static",marker='o',markersize=16,linewidth=2.0,linestyle='--')
plt.xticks([i for i in range(0,17,2)],fontsize=20)
plt.yticks([i for i in range(0,500000,50000)],fontsize=20)
plt.xlabel("第几个周期/10s", fontdict = { 'size' : 24 })
plt.ylabel("负载均衡比变化曲线", fontdict = { 'size' : 24 })
plt.legend(fontsize=20)
plt.show()

