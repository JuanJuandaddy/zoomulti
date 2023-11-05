# -*-coding:utf-8-*-
# -*-this is a python script -*-
#指定表结构
from sqlalchemy.orm import declarative_base, relationship  # 调用ORM基类
from sqlalchemy import Column,String,Integer,Float
from connect import ConnectDB
engine=ConnectDB().get_engine()
Base=declarative_base()
#每一张表都是一个类
class Controller(Base):
    __tablename__="controller"
    controller_id=Column(Integer,primary_key=True,comment="控制器ID",index=True)#设控制器ID为主键,并为索引
    packet_in_load=Column(Float,comment="packetin负载")
    packet_in_delay=Column(Float,comment="packetin处理延迟")
    switches_load=relationship('SwitchesLoad')
    def __init__(self):
        pass
    def __repr__(self):
        #返回的对象格式
        return f"<{self.__class__.__name__}(controller_id={self.controller_id}," \
               f"packet_in_load={self.packet_in_load},packet_in_delay={self.packet_in_delay})>"
class SwitchesLoad(Base):
    __tablename__="switches_load"
    id=Column(Integer,primary_key=True)
    master_controller=Column(Integer)
    packet_in_speed=Column(Float)
    packet_in_size=Column(Float)
    packet_in_percentage=Column(Float)

    def __init__(self):
        pass
    def __repr__(self):
        #返回的对象格式
        return f"<{self.__class__.__name__}(master_controller={self.controller_id}," \
               f"packet_in_speed={self.packet_in_speed},packet_in_size={self.packet_in_size}," \
               f"packet_in_percentage={self.packet_in_percentage})>"

class CreateTables(object):
    def __init__(self,engine):
        self.engine=engine

    def create(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    CreateTables(engine=engine).create()