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

def generate_combinations(arr,load):
    def backtrack(start, path):
        combinations.append(path[:])
        for i in range(start, len(arr)):
            path.append(arr[i])
            print(path)
            
            backtrack(i + 1, path)
            
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations