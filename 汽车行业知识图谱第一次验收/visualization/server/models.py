# -*- coding: utf-8 -*- 
# @Author: Shuang0420 
# @Date: 2017-08-29 17:08:03 
# @Last Modified by:   Shuang0420 
# @Last Modified time: 2017-08-29 18:58:13 


import json
import json
import pymysql
import sys
import os
from conf import *

fname = os.getcwd() + json_path

edge_sql_car = """select a.attribute_name,a.attribute_value from car_node n,car_node_attribute a where n.id = a.node_id and n.name = '%s';""" 
edge_sql_relation = """SELECT subj, obj, pred, company.company_name, company.code, person.name, type FROM spo JOIN company JOIN person WHERE spo.subj=company.id AND spo.obj=person.id AND person.name="%s";"""
secondary_edge_sql = 'SELECT * FROM spo WHERE subj="%s"'

def execute(database, attr):
    js = {}
    edges=[]
    try:
        if attr[0]=='car_name':
            sql = edge_sql_car%(attr[1])  
            count=database.cursor.execute(sql)
            if count != 0:
                for result in database.cursor.fetchall():
                    print(result)
                    edges.append({"source": attr[1], "target": result[1], "relation": result[0], "label": 'relation'})
            else:
                print('car_name不存在')	
    except:
        print("ERROR: " + sql)
        database.conn.rollback()
    # js["nodes"] = nodes
    js["edges"] = edges
    mydata = json.dumps(js, ensure_ascii=False).encode("utf8")
    print('Json路径是:%s'%(fname))
    with open(fname, 'w',encoding='utf-8') as f:
        f.write(str(mydata))
    return mydata
