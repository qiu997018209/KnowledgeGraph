#coding:utf-8
'''
Created on 2017年12月11日

@author: qiujiahao

@email:997018209@qq.com

'''
import pymysql
import os
from conf import *

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

    
if __name__=='__main__':
    database=database()           