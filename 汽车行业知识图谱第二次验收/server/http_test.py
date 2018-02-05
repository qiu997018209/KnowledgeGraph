#coding:utf-8
'''
Created on 2017年10月9日

@author: qiujiahao

@email:997018209@qq.com

'''
import requests
import json
s = requests
lookup_entry={"method":'entry','id':1,'jsonrpc':2.0,"params":{'name':'英朗','deep':3}}
lookup_statistics={"method":'statistics','id':1,'jsonrpc':2.0}
lookup_entry2entry={"method":'entry_to_entry','id':1,'jsonrpc':2.0,"params":{'entry1':'英朗','entry2':'前轮驱动'}}
lookup_entry2property={"method":'entry_to_property','id':1,'jsonrpc':2.0,"params":{'entry':'英朗','property':'驱动方式'}}


while True:
    choice=input('你想测试的方法是:\n1.entry\n2.statistics\n3.entry2entry\n4.entry2property\n:')
    if choice=='1':
        data=lookup_entry
    elif choice=='2':
        data=lookup_statistics
    elif choice=='3':
        data=lookup_entry2entry
    elif choice=='4':
        data=lookup_entry2property
    try:
        r = s.post('http://192.168.1.245:1111/KnowGraph/v2', json.dumps(data))
        print (r.status_code)
        print (r.headers['content-type'])
        r.encoding = 'utf-8'
        print (eval(r.text))
    except Exception as e:
        print(e)
