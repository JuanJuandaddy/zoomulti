# -*-coding:utf-8-*-
# -*-this is a python script -*-
from pymysql import Connect
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from db import config
connect_sentence=f'mysql+pymysql://hcielw:000000@localhost:3306/sdn?charset=utf8'
class ConnectDB(object):
    def __init__(self):
        self.engine=create_engine(connect_sentence,echo=True,pool_size=0,pool_recycle=60*60,poolclass = QueuePool)
    def get_engine(self):
        return self.engine
    def get_session(self):
        return sessionmaker(bind = self.engine)
db=ConnectDB()

engine=db.get_engine()
session=db.get_session()()