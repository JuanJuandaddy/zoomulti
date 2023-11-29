# -*-coding:utf-8-*-
# -*-this is a python script -*-
#数据库配置文件
db_ip='localhost'
db_port=3306
db_name='sdn'
db_user='hcielw'
db_passwd=000000

table_template="flow_table:src_host={src},dst_host={dst},outport={outport}," \
               "priority={priority},protocol={protocol},idle_timeout={idle_timeout},hard_timeout={hard_timeout}"