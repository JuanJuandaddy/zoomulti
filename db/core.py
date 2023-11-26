# -*-coding:utf-8-*-
# -*-this is a python script -*-
from connect import session
from models import *
from typing import  Dict,List
#CURD功能组

def Save_Switches_Map(status:Dict[int,List]):
	# 控制器控制的交换机表 {c1:[s11,s12]....}
	sql = """
    INSERT INTO switches_map (switch, master) 
    VALUES (:switch, :master) 
    ON DUPLICATE KEY UPDATE master = :master;
    """
	def bulk_operation(data:List[Dict]):
		session.execute(sql, data)
		session.commit()
	try :
		bulk = []
		for k, v in status.items() :
			for sw in v:
				bulk.append({
					"switch":f's{sw}',
					"master":k
				})
				bulk_operation(bulk)

	except Exception as e :
		raise e
def Save_Switches_Status(status:Dict[int,Dict]):
	
	##{c1:{sw1:{pktin_speed:xxx,percentage：xxx,pktin_size:xxx}....}}
	try:
		bulk=[]
		for k,v in status.items():
			bulk.append({
			
			})
		
		session.bulk_insert_mappings(SwitchesStatus,bulk)
	except Exception as e:
		raise e
	else:
		session.commit()


def Save_Controller_Status (status:Dict[int,Dict]) :
	# {c1:{pktin:xxx,delay:xxx}}
	try :
		
		bulk=[]
		for k,v in status.items():
			
			bulk.append({
				"name":f'controller{k}',
				"packetin":v.get('pktin',0),
				"loadrate" : round(v.get('pktin', 0)/1600,5),
				"controller_id":k
			})
			
		session.bulk_insert_mappings(ControllerStatus,bulk)
	except Exception as e :
		raise e
	else :
		session.commit()
