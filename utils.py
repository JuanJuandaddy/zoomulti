# -*-coding:utf-8-*-
# -*-this is a python script -*-
#工具函数
import numpy as np
from prettytable import PrettyTable
from typing import List,Dict
def display_controller_load(controller_load:Dict):
    #显示控制器负载总体信息
    table = PrettyTable(['控制器', 'PacketIn速度/s', 'PacketIn处理时延/ms'])

    table.add_rows([[k,v["pktin"],v["delay"]] for k,v in controller_load.items()])
    print(table)
def display_controller_sw_load(controller_sw_load:Dict):
    #显示控制器负载的详细信息
    table=PrettyTable(['所属控制器','交换机编号','PacketIn速度/s','PacketIn大小/bytes','PacketIn占比'])
    for controller,sw_load in controller_sw_load.items():
        table.add_rows([[controller,k,v["pktin_speed"],v["pktin_size"],v["percentage"]] for k,v in sw_load.items()])
    print(table)

def display_cluster_status(avg_load:float,variance:float):
    #显示集群状态
    table = PrettyTable(['集群平均负载/packet/s','集群负载均衡度'])
    table.add_row([avg_load,variance])
    print(table)
def display_migration_plan(src,plan:Dict):
    #显示迁移计划
    m_set= plan.get('migration_set')
    table = PrettyTable(['迁移方案序号','迁出控制器','迁出交换机序号','迁入控制器'])
    table.add_rows([[i+1,src,m_set[i],plan.get('dest_controller')] for i in range(len(m_set))])
    print(table)

def strip_s(sw:str):
    return int(sw.strip('s'))

def strip_c(controller:str):
    return int(controller.strip('c'))

def generate_combinations(arr:List,sw_load:Dict):
    def backtrack(start, path,sw):
        combinations.append(path[:])
        sw_list.append(sw[:])
        for i in range(start, len(arr)):
            path.append(arr[i])
            for k,v in sw_load.items():
                if v[1]==arr[i] and v[0] not in sw:
                    sw.append(v[0])
            backtrack(i + 1, path,sw)
            path.pop()
            sw.pop()
    sw_list=[]
    combinations = []
    backtrack(0, [],[])
    return combinations[1:],sw_list[1:]

