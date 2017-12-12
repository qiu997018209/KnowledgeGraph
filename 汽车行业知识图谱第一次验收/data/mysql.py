#coding:utf-8
'''
Created on 2017年12月11日

@author: qiujiahao

@email:997018209@qq.com

'''
import pymysql
import os
import sys
sys.path.append("..")
from conf import *

car_node='''
create table car_node(
    id int primary key NOT NULL AUTO_INCREMENT,
    name varchar(100),
    ext  varchar(500),
    create_time DATETIME,
        create_id INT(32),
        update_time DATETIME,
        update_id INT(32),
        is_delete INT DEFAULT '0' NOT NULL
);
'''
car_node_attribute='''
create table car_node_attribute(
    id int primary key NOT NULL AUTO_INCREMENT,
    node_id int not null,
    attribute_name varchar(200),
    attribute_value varchar(200),
    is_delete INT DEFAULT '0' NOT NULL
);
'''
class database(object):
    def __init__(self):
        self.conn = pymysql.connect(
                host = MYSQL_HOST,
                port = MYSQL_PORT,
                user = MYSQL_USER,
                password = MYSQL_PASSWORD,
                charset ='utf8',
                db = MYSQL_db)
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.conn.close()
    def data_process(self):
        with open(os.path.join(DATA_PATH,'..','three_tuples.txt'),'r',encoding='utf-8') as f:
            for line in f.readlines():
                line=self.clean_string(line).split(':')
                if len(line)!=3:
                    continue 
                mysql_cmd="select id from car_node where name='%s';"%(line[0])
                count=self.cursor.execute(mysql_cmd)
                if(count==0):
                    mysql_cmd="insert into car_node(name) values('%s');"%(line[0])
                    self.cursor.execute(mysql_cmd)
                    node_id=self.conn.insert_id()
                    #print(node_id,line[1],line[2])
                    mysql_cmd='''insert into car_node_attribute(node_id,attribute_name,attribute_value)  values(%d,'%s','%s');'''%(node_id,line[1],line[2])
                    self.cursor.execute(mysql_cmd)                                
                else:
                    result=self.cursor.fetchone()
                    node_id=result[0]
                    mysql_cmd='''insert into car_node_attribute
                    (node_id,attribute_name,attribute_value)  values(%d,'%s','%s');'''%(node_id,line[1],line[2]) 
                    print(mysql_cmd)
                    self.cursor.execute(mysql_cmd)      
        self.conn.commit()
            
    def clean_string(self,value):
        if(value=='' or value==None):
            return
        value=value.strip().replace('\'','')
        return value
    
if __name__=='__main__':
    database=database()
    database.data_process()
   
            