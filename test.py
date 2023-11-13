import re
import pickle
from random import Random
import exp_conf
import json
def get_random_red_packet (total_amount, quantities) :
	# 发红包逻辑
	amount_list = []
	person_num = quantities
	cur_total_amount = total_amount
	for _ in range(quantities - 1) :
		amount = Random().randint(0, cur_total_amount // person_num * 2)
		# 每次减去当前随机金额，用剩余金额进行下次随机获取
		cur_total_amount -= amount
		person_num -= 1
		amount_list.append(amount)
	amount_list.append(cur_total_amount)
	return amount_list

HOSTS=[[['h1001', 'h1002', 'h1003'], ['h1101', 'h1102', 'h1103'], ['h1201', 'h1202', 'h1203'], ['h1301', 'h1302', 'h1303'], ['h1401', 'h1402', 'h1403'], ['h1501', 'h1502', 'h1503'], ['h1601', 'h1602', 'h1603']],
       [['h2001', 'h2002', 'h2003'], ['h2101', 'h2102', 'h2103'], ['h2201', 'h2202', 'h2203'], ['h2301', 'h2302', 'h2303'], ['h2401', 'h2402', 'h2403'], ['h2501', 'h2502', 'h2503'], ['h2601', 'h2602', 'h2603']],
       [['h3001', 'h3002', 'h3003'], ['h3101', 'h3102', 'h3103'], ['h3201', 'h3202', 'h3203'], ['h3301', 'h3302', 'h3303'], ['h3401', 'h3402', 'h3403']],
       [['h4001', 'h4002', 'h4003'], ['h4101', 'h4102', 'h4103'], ['h4201', 'h4202', 'h4203'], ['h4301', 'h4302', 'h4303'], ['h4401', 'h4402', 'h4403'], ['h4501', 'h4502', 'h4503'], ['h4601', 'h4602', 'h4603'], ['h4701', 'h4702', 'h4703']],
       [['h5001', 'h5002', 'h5003'], ['h5101', 'h5102', 'h5103'], ['h5201', 'h5202', 'h5203'], ['h5301', 'h5302', 'h5303'], ['h5401', 'h5402', 'h5403'], ['h5501', 'h5502', 'h5503'], ['h5601', 'h5602', 'h5603']]]
dict={}
controller_load=exp_conf.controller_load
for controller,host in enumerate(HOSTS):
	sum_load=controller_load[f'c{controller+1}']
	
	load_map=get_random_red_packet(sum_load//10,len(host))
	for h,pktin in zip(host,load_map):
		dict[h[0]]=int(pktin*10)
with open('exp_conf.py','w') as f:
	f.write(f'controller_load={json.dumps(controller_load)}')
	f.write('\n')
	f.write(f'config={json.dumps(dict)}')


