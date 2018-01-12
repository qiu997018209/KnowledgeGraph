#coding:utf-8
'''
Created on 2018年1月12日

@author: qiujiahao

@email:997018209@qq.com

'''



import json
import requests

#查询实体
url='http://shuyantech.com/api/cndbpedia/avpair'
quest={'q':'复旦大学'}
print(requests.post(url,quest).text)

#查询概念
url='http://shuyantech.com/api/cnprobase/concept'
quest={'q':'刘德华'}
print(requests.post(url,quest).text)