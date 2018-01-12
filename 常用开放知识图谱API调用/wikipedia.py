#coding:utf-8
'''
Created on 2018年1月12日

@author: qiujiahao

@email:997018209@qq.com

介绍:https://github.com/goldsmith/Wikipedia
'''
import wikipedia 

def show(data):
    try:
        print('title',data.title)#标题
        print('title',data.url)#页面url
        print('title',data.content)#页面内容
        print('title',data.links[0])#页面连接
    except:
        print(data)
    
wikipedia.set_lang('zh')#设置语言
print(wikipedia.search('中山大小'))#搜索
my=wikipedia.page('中山大小')#获取页面
show(my)
