# -*-coding:utf-8-*-
# -*-this is a python script -*-
#指定表结构
import time

from sqlalchemy.orm import declarative_base, relationship,Session  # 调用ORM基类
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, UniqueConstraint
from connect import engine
engine=engine
Base=declarative_base()
#每一张表都是一个类,定义了一些表结构,所有的auto字段可以不指定
class User(Base):
    __tablename__="user"
    username=Column(String(255),primary_key=True,comment="用户名",unique = True)#设控制器ID为主键,并为索引
    password=Column(String(255),comment="密码")
    access=Column(String(255),comment="权限")
    def __init__(self):
        pass
class SwitchesStatus(Base):
    __tablename__="switches_status"
    dpid=Column(Integer,primary_key=True,index = True,unique = True)
    packetin=Column(Float,default = 0)
    master=Column(Integer)
    def __init__(self):
        pass
class FlowTables(Base):
    id=Column(Integer,primary_key = True,autoincrement = True)
    __tablename__ = "flow_tables"
    table=Column(String(255))
    dpid=Column(Integer,index = True,unique = True)
    def __init__(self):
        pass
class ControllerStatus(Base) :
    __tablename__ = "controller_status"
    id = Column(Integer, primary_key = True,autoincrement = True)
    name=Column(String(255),unique = True)
    controller_id=Column(Integer,index = True,unique = True,primary_key = True)
    packetin=Column(Float,default = 0)
    loadrate=Column(Float,default = 0)
    def __init__(self):
        pass
class SwitchesMap(Base):
    __tablename__ = "switches_map"
    id = Column(Integer, primary_key = True,autoincrement = True)
    switch = Column(String(255),unique = True)
    master = Column(Integer, index = True)
    def __init__(self):
        pass
class LinkStatus(Base) :
    __tablename__ = "link_status"
    id = Column(Integer, primary_key = True,autoincrement = True)
    srcnode = Column(String(255))
    dstnode = Column(String(255))
    userate=Column(Float,default = 0)
    droprate = Column(Float, default = 0)
    portspeed = Column(Float, default = 0)
    def __init__(self):
        pass
class NetworkStatus(Base) :
    __tablename__ = "network_status"
    id = Column(Integer, primary_key = True,autoincrement = True)
    linkuserate=Column(Float,default = 0)
    throughoutput=Column(Float,default = 0)
    def __init__(self):
        pass
class RouteStatus(Base) :
    __tablename__ = "route_status"
    id = Column(Integer, primary_key = True,autoincrement = True)
    srcnode=Column(String(255))#必须是主机节点
    dstnode=Column(String(255))#必须是主机节点
    currentpath=Column(String(255))#转发路径
    __table_args__ = (UniqueConstraint('srcnode', 'dstnode'),)#表示该组合组成的键值是唯一的
    def __init__(self):
        pass
class CreateTables(object):
    def __init__(self,engine):
        self.engine=engine

    def create(self):
        Base.metadata.create_all(self.engine)
    def delete_all_tables(self):
        if input("该操作会删除数据库中全部的表，请按y确定\n请输入： ").__eq__('y'):
            Base.metadata.drop_all(self.engine)
        else:
            print("操作失败")

if __name__ == '__main__':
    pass
    obj=CreateTables(engine=engine)
    #obj.create()
    obj.delete_all_tables()
