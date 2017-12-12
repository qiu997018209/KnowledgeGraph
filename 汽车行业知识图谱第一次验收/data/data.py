#coding:utf-8
'''
Created on 2017年11月27日

@author: qiujiahao

@email:997018209@qq.com

'''
import os
import re
import sys
sys.path.append("..")
from conf import *
from bs4 import BeautifulSoup

class data(object):
    def __init__(self):
        #self.database=database()
        self.process_cars()
    def process_cars(self):
        #连接数据库 
        f= open(os.path.join(DATA_PATH,'..','three_tuples.txt'),'w',encoding='utf-8')       
        for _,_,files in os.walk(DATA_PATH):
            for file in files:
                print('进度:%s:%d/%d'%(file,files.index(file)+1,len(files)))
                my_data=self.process_html(file)
                if(my_data==None):
                    continue
                for data in my_data:
                    f.write('%s:%s:%s\n'%(data[0],data[1],data[2]))
                    
                #self.database.execute(car_info)
        #解析每一个html
    def process_html(self,file):
        file = open(os.path.join(DATA_PATH,file),'r',encoding='utf-8')
        my_data=set()
        soup=BeautifulSoup(file,'html.parser', from_encoding='utf-8')

        main_key=soup.find('title')
        if main_key==None:
            return None
        main_key=self.clean_string(main_key.string)
        names=[]
        for value in soup.find_all('dt',class_='basicInfo-item name'):
            names.append(self.clean_string(value.string))
        values=[]
        for value in soup.find_all('dd',class_='basicInfo-item value'):
            if value.string==None:
                values.append(self.clean_string(value.get_text()))
            else:
                values.append(self.clean_string(value.string)) 
        if(len(values)!=len(names)):
            my_data=[]
            return                  
        for name in names:
            value=values[names.index(name)]  
            my_data.add((main_key,name,value))
            #print(my_data[0])
        return my_data    
    
    def clean_string(self,value):
        if(value=='' or value==None):
            return
        value=value.strip().replace(' ','').upper()
        value = re.compile(r"_百度百科").sub('',value)
        value = re.compile(r"\[.*\]").sub('',value)
        value = re.compile(r"\(.*\)").sub('',value)
        value = re.compile(r"\（.*\）").sub('',value)
        value = re.compile(r"    ").sub('',value)
        return value
                    
if __name__ == "__main__":
    data=data()

    










