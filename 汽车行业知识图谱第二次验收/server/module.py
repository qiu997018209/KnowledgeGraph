# -*- coding: utf-8 -*- 
import tensorflow as tf
import numpy as np
import os
import time
from threading import Thread
from py2neo import Node,Relationship,size,order,Graph,NodeSelector

class KnowGraph(object):
    def __init__(self,args):
        self.args=args
        self.graph = Graph('127.0.0.1:7474',user='neo4j',password='123456')
        self.write_to_statistics()
    #查找单个实体
    def lookup_entry(self,client_params,server_param):
        #支持设定网络查找的深度
        start_time = time.time()
        params=client_params["params"]
        edges=set()
        self.lookup_entry_deep(edges,params,0)
        if len(edges)==0:
            server_param['result']={"success":'false'}
        else:                
            server_param['result']={'edges':[list(i) for i in edges],"success":'true'}
            print('本次查找三元组的数量为:{},耗时:{}s'.format(len(edges),time.time()-start_time))
        
    #查找两个实体间的关系
    def lookup_entry2entry(self,client_params,server_param):
        params=client_params["params"]
        edges=set()
        
        #考虑到顺序的问题，所以查了四次
        result1=self.graph.data("MATCH (s)-[r]->(e) where s.name='{}' and e.name='{}' RETURN s.name,r.name,e.name".format(params['entry1'],params['entry2']))
        result2=self.graph.data("MATCH (s)-[r]->(e) where s.name='{}' and e.name='{}' RETURN s.name,r.name,e.name".format(params['entry2'],params['entry1']))

        if len(result1)==0 and len(result2)==0:
            server_param["result"]={"success":'false'}
            return
        for item in result1:
            edges.add((item['s.name'],item['r.name'],item['e.name']))
        for item in result2:
            edges.add((item['s.name'],item['r.name'],item['e.name']))           
        
        #result=self.graph.data("match (a),(b) where a.name='{}' and b.name='{}' match p = shortestPath((a)-[*..15]-(b))return p".format(params['entry1'],params['entry2']))                
        server_param["result"]={'edges':[list(i) for i in edges],"success":'true'}  
        
    #查找指定实体的指定属性
    def lookup_entry2property(self,client_params,server_param):
        params=client_params["params"]
        edges=set()
        result1=self.graph.data("MATCH (s)-[r]->(e) where s.name='{}' and r.name='{}' RETURN s.name,r.name,e.name".format(params['entry'],params['property']))
        result2=self.graph.data("MATCH (e)<-[r]-(s) where e.name='{}' and r.name='{}' RETURN s.name,r.name,e.name".format(params['entry'],params['property']))
        if len(result1)==0 and len(result2)==0:
            server_param["result"]=[{"success":'false'}]
            return
        for item in result1:
            edges.add((item['s.name'],item['r.name'],item['e.name']))
        for item in result2:
            edges.add((item['s.name'],item['r.name'],item['e.name']))            
        server_param["result"]={'edges':[list(i) for i in edges],"success":'true'} 
         
    #查询统计信息
    def lookup_statistics(self,client_params,server_param):
        result=self.graph.data("MATCH (n) RETURN n")
        with open('../data/statistics.txt','r',encoding='utf-8') as f:
            api_nums=f.readline().strip()
        server_param['result']={'total_nums':len(result),'api_nums':api_nums,"success":'true'}
   
    #统计API访问次数      
    def write_to_statistics(self):
        with open('../data/statistics.txt','r',encoding='utf-8') as f:
            api_nums=int(f.readline().strip())+1
        with open('../data/statistics.txt','w',encoding='utf-8') as f:
            f.write(str(api_nums)+'\n')
       
    #限制深度的查找
    def lookup_entry_deep(self,edges,params,deep):
        #当前查找深度不得等于要求的深度
        if deep >= params['deep']:
            return
        #正向查找
        result1=self.graph.data("match (s)-[r]->(e) where s.name='{}' return s.name,r.name,e.name".format(params['name']))
        result2=self.graph.data("match (e)<-[r]-(s) where e.name='{}' return s.name,r.name,e.name".format(params['name']))
        if len(result1)==0 and len(result2)==0:
            return
        for item in result1:
            edges.add((item['s.name'],item['r.name'],item['e.name']))
            if  item['s.name'] != item['e.name']:#避免出现:双面胶:中文名:双面胶的死循环
                params['name']=item['e.name']
                self.lookup_entry_deep(edges,params.copy(),deep+1)
 
        for item in result2:
            edges.add((item['s.name'],item['r.name'],item['e.name']))
            if  item['s.name'] != item['e.name']:#避免出现:双面胶:中文名:双面胶的死循环
                params['name']=item['e.name']
                self.lookup_entry_deep(edges,params.copy(),deep+1)       
                                    