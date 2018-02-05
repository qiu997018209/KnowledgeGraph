#coding:utf-8
'''
Created on 2018年1月26日

@author: qiujiahao

@email:997018209@qq.com

'''
import sys
import re
sys.path.append('..')
from conf import get_args
from py2neo import Node,Relationship,size,order,Graph,NodeSelector

class data(object):
    def __init__(self):
        self.args=get_args()
        self.data_process()
        
    def data_process(self):
        #初始化操作
        self.data_init()
        
        #插入数据
        self.insert_datas()
        
        
    def data_init(self):
        #连接图数据库
        print('开始数据预处理')
        self.graph = Graph('127.0.0.1:7474',user=self.args.neo4j_user,password=self.args.neo4j_password)
        self.selector=NodeSelector(self.graph)
        self.graph.delete_all()
        
    def insert_datas(self):
        print('开始插入数据')
        with open('../data/three_tuples.txt','r',encoding='utf-8') as f:
            lines,num=f.readlines(),-1
            for line in lines:
                num+=1
                if num%500==0:
                    print('当前处理进度:{}/{}'.format(lines.index(line),len(lines)))
                line=line.strip().split('\t')
                if len(line)!=3:
                    print('insert_datas错误:',line)
                    continue
                self.insert_one_data(line)
                    
                    
    def insert_one_data(self,line):
        if '' in line:
            print('insert_one_data错误',line)
            return

        start=self.look_and_create(line[0])
        for name in self.get_items(line[2]):
            end=self.look_and_create(name)
            r=Relationship(start,line[1],end,name=line[1])   
            self.graph.create(r)#当存在时不会创建新的
        
        #查找节点是否不存，不存在就创建一个
    def look_and_create(self,name):
        end=self.graph.find_one(label="car_industry",property_key="name",property_value=name)
        if end==None:
            end=Node('car_industry',name=name)           
        return end 
    
    def get_items(self,line):  
        if '{' not in line and '}' not in line:
            return [line]
        #检查
        if '{' not in line or '}' not in line:
            print('get_items Error',line)
        lines= [w[1:-1] for w in re.findall('{.*?}',line)] 
        return lines 
    
if __name__=='__main__':
    data=data()                   
                    
