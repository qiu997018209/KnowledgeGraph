#coding:utf-8
'''
Created on 2018年1月9日

@author: qiujiahao

@email:997018209@qq.com

'''
 
from flask import jsonify
from conf import *
from flask import Flask
from flask import request
from server.app import app
import tensorflow as tf
from server.module import KnowGraph
import json 

@app.route('/KnowGraph/v2',methods=["POST"])
def look_up():
    kg=KnowGraph(get_args())
    client_params=request.get_json(force=True)
    server_param={}
    if client_params['method'] == 'entry_to_entry':
        kg.lookup_entry2entry(client_params,server_param)
    elif client_params['method'] == 'entry_to_property':
        kg.lookup_entry2property(client_params,server_param)
    elif client_params['method'] == 'entry':
        kg.lookup_entry(client_params,server_param)
    elif client_params['method'] == 'statistics':
        kg.lookup_statistics(client_params,server_param)
    elif client_params['method'] == 'live':
        params={'success':'true'}
        server_param['result']=params    
    server_param['id']=client_params['id']
    server_param['jsonrpc']=client_params['jsonrpc']
    server_param['method']=client_params['method']
    print(server_param)
    return json.dumps(server_param, ensure_ascii=False).encode("utf-8")