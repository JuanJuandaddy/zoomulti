# 原始字典
import numpy as np

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
print(sorted_sw_load)
print(sw_load)
print(load_list)
__import__('utils').generate_combinations(load_list,70)


#




