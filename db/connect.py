# -*-coding:utf-8-*-
# -*-this is a python script -*-
from pymysql import Connect
from sqlalchemy import create_engine
from db import config
connect_sentence=f'mysql+pymysql://hcielw:000000@localhost:3306/cluster?charset=utf8'
class ConnectDB(object):
    def __init__(self):
        self.engine=create_engine(connect_sentence,echo=True,pool_size=0,pool_recycle=60*60)
    def get_engine(self):
        return self.engine