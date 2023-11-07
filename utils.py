# -*-coding:utf-8-*-
# -*-this is a python script -*-
def display_controller_load(controller_load:dict):
    print("c_name |    pktin    |    delay")
    for k,v in controller_load.items():
        print(f'  {k}   |     {v["pktin"]}    |    {v["delay"]}')

def strip_s(sw:str):
    return int(sw.strip('s'))

def strip_c(controller:str):
    return int(controller.strip('c'))

def generate_combinations(arr,sw_load):
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
    return combinations,sw_list