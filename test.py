# 原始字典
import numpy as np
from typing import List
original_dict = {
    10: {'pktin_speed': 2.2},
    11: {'pktin_speed': 0.4},
    12: {'pktin_speed': 0.8},
    13: {'pktin_speed': 1.2},
    14: {'pktin_speed': 1.2},
    15: {'pktin_speed': 115.8},
    16: {'pktin_speed': 2.4},
}

# 按照pkt的值从大到小排序
sorted_sw_load = {k: v for k, v in sorted(original_dict.items(), key=lambda item: item[1]['pktin_speed'], reverse=True)}

# 创建新的字典，格式为{（order，sw）: pkt的值}
sw_load = {i + 1: (k, v['pktin_speed']) for i, (k, v) in enumerate(sorted_sw_load.items())}

# 转化为列表
load_list = [sw_load[i+1][1] for i, k in enumerate(sorted_sw_load.keys())]


def update_controller_to_switches ( src: int, dst: int, m_set: List) :
    if src == dst :
        return
    for sw in m_set :
        controllers[src].remove(sw)
        #sw not in controllers[dst] :
        controllers[dst].append(sw)

src,dst=1,2
controllers={
    1:[3,4,5],
    2:[7,8,9]
}
update_controller_to_switches(src,dst,m_set = [4])
print(controllers)
update_controller_to_switches(src,dst,m_set = [3])
print(controllers)
update_controller_to_switches(dst,src,m_set = [4])
print(controllers)


