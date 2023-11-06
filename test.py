# 原始字典
original_dict = {
    'sw1': {'pkt': 100},
    'sw2': {'pkt': 200},
    'sw3': {'pkt': 50},
}

# 按照pkt的值从大到小排序
sorted_dict = {k: v for k, v in sorted(original_dict.items(), key=lambda item: item[1]['pkt'], reverse=True)}

# 创建新的字典，格式为{（order，sw）: pkt的值}
new_dict = {f'({i+1}, {k})': v['pkt'] for i, (k, v) in enumerate(sorted_dict.items())}

# 转化为列表
result_list = [new_dict[f'({i+1}, {k})'] for i, k in enumerate(sorted_dict.keys())]
print(sorted_dict)
print(new_dict)
print(result_list)
