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