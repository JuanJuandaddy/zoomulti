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

	try :
		bulk = []
		for controller, switches in status.items() :
			for sw in switches:
				bulk.append({
					"switch":f's{sw}',
					"master":controller
				})
		bulk_operation(bulk)

	except Exception as e :
		raise e
def Save_Switches_Status(status:Dict[int,Dict[int,Dict]]):
	
	##{c1:{sw1:{pktin_speed:xxx,percentage：xxx,pktin_size:xxx}....}}
	sql =  """
		    INSERT INTO switches_status (dpid, packetin, master)
		    VALUES (:dpid, :packetin, :master)
		    ON DUPLICATE KEY UPDATE packetin = :packetin, master = :master;
            """

	def bulk_operation (data: List[Dict]) :
		session.execute(sql, data)

	try:
		bulk=[]
		for controller,switches in status.items():
			for sw,info in switches.items():
				bulk.append({
					"dpid":f's{sw}',
					"packetin":info.get('pktin_speed'),
					"master":controller
				})
		
		bulk_operation(bulk)
	except Exception as e:
		raise e
	else:
		session.commit()
def Save_Controller_Status (status:Dict[int,Dict]) :
	# {c1:{pktin:xxx,delay:xxx}}
	sql = """
	    INSERT INTO controller_status (name, controller_id, packetin, loadrate)
	    VALUES (:name, :controller_id, :packetin, :loadrate)
	    ON DUPLICATE KEY UPDATE packetin = :packetin, loadrate = :loadrate;
    """
	
	def bulk_operation (data: List[Dict]) :
		session.execute(sql, data)
		
	try :
		
		bulk=[]
		for controller,load in status.items():
			bulk.append({
				"name":f'controller{controller}',
				"packetin":load.get('pktin',0),
				"loadrate" : round(load.get('pktin', 0)/1600,5),
				"controller_id":controller
			})
		bulk_operation(bulk)
	except Exception as e :
		raise e
	else :
		session.commit()
def Save_Flow_Tables(status:List[Dict]):
	#status:[{dpid:table}.....]
	sql="""
		INSERT INTO flow_tables (dpid, table)
	    VALUES (:dpid, :table)
	    ON DUPLICATE KEY UPDATE dpid = :dpid, table = :table;
    """
	def bulk_operation (data: List[Dict]) :
		session.execute(sql, data)
	try:
		bulk_operation(status)
	except Exception as e:
		raise e
	else:
		session.commit()
def Save_Route_Status(status:Dict):
	sql = """
			INSERT INTO flow_tables (dpid, table)
		    VALUES (:dpid, :table)
		    ON DUPLICATE KEY UPDATE dpid = :dpid, table = :table;
	    """
	
	def bulk_operation (data:Dict) :
		session.execute(sql, data)
	
	try :
		bulk_operation(status)
	except Exception as e :
		raise e
	else :
		session.commit()