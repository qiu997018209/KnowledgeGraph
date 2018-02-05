#coding:utf-8
'''
Created on 2017年12月11日

@author: qiujiahao

@email:997018209@qq.com

'''
#数据路径

import argparse

def get_args():
    parser = argparse.ArgumentParser() 
    parser.add_argument('-nu','--neo4j_user', help='neo4j的用户名',type=str,default='neo4j')
    parser.add_argument('-np','--neo4j_password', help='neo4j的密码',type=str,default='123456')
    parser.add_argument('-p','--http_port', help='http端口',type=int,default='8080')
    args = parser.parse_args()
    return args




