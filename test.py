import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
plt.rcParams['font.sans-serif']='SimHei'
import numpy as np
plt.figure(figsize = (20, 10), dpi = 100)
x=[0.08,0.17,0.24,0.61,0.7,0.97,3.40]
y= [100,400,700,1000,1300,1600,1900]
plt.plot(y, x, c = 'red')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("PacketIn速率", fontdict = { 'size' : 24 })
plt.ylabel("控制器处理单个PacketIn平均延迟/ms", fontdict = { 'size' : 24 })
plt.legend()
plt.show()