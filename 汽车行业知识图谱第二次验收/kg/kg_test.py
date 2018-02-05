#coding:utf-8
'''
Created on 2018年1月25日

@author: qiujiahao

@email:997018209@qq.com

'''
from py2neo import Node,Relationship,size,order,Graph,NodeSelector

#graph = Graph('127.0.0.1:7474',user='neo4j',password='123456')
'''
常用API
graph.delete_all() 删除所有的节点和关系
graph.data("MATCH (n) RETURN n") 调用Cypher查询语言

a=Node('Person',name='Mike',age=21,location='广州')
b=Node('Person',name='Bob',age=22,location='上海')
c=Node('Person',name='Alice',age=21,location='北京')
r1=Relationship(a,'KNOWS',b)
r2=Relationship(b,'KNOWS',c)
graph.create(a|b|c|r1|r2)

selector=NodeSelector(graph)#会找出所有的关系
#persons=selector.select('Person',age=21)
#print(list(persons))
#使用正则表达式进行查找
persons=selector.select('Person').where("_.name =~ 'A.*'")
print(list(persons))
#查找单个节点
persons=selector.select('Person').where("_.name =~ 'A.*'").first()
print(list(persons))

#查找一个
relations=graph.match_one(rel_type='KNOWS')
print(relations)

#排序
selector=NodeSelector(graph)#会找出所有的关系
persons=selector.select('Person').order_by('_.age')
print(list(persons))

#运行Cyper语句
data=graph.run('MATCH (p:Person) RETURN p LIMIT 5')
print(list(data))

'''
'''
#OGM可以实现一个对象和Node的关联
from py2neo.ogm import GraphObject,Property,RelatedTo

class Person(GraphObject):
    __primarykey__='name'#默认是id,设置主键的好处是push数据的时候不会重复添加
    name=Property()
    age=Property()
    location=Property()
    knows=RelatedTo('Person','KNOWS')
    
person=Person.select(graph).where(age=20).first()
print(person)
print(person.name)
print(person.location)
person.age=20
print(person.__ogm__.node)
graph.push(person)
print(list(person.knows))

new_person=Person()
new_person.name='Durant'
new_person.age=28
person.knows.add(new_person)
print(list(person.knows))
graph.push(person)#添加到数据库

target=Person.select(graph).where(name='Durant').first()
print(list(person.knows))
person.knows.remove(target)#删除节点间的关系
print(list(person.knows))

graph.push(person)
graph.delete(target)#先删除节点上的关系，才能删除节点

graph.delete_all()
b=Node('Person',name='Bob',age=22,location='上海')
a=Node('Person',name='Bob2',age=22,location='上海')
c=Node('Person',name='Bob2',age=22,location='上海')
r1=Relationship(a,'KNOWS',b)
graph.create(r1)
r2=Relationship(a,'KNOWS',c)
graph.create(r2)

c=Node('Person',name='Bob3',age=22,location='上海')
r1=Relationship(a,'KNOWS',c)
graph.create(r1)
r1=Relationship(c,'KNOWS',b)
graph.create(r1)
#graph.push(b) 
'''
'''
with open('../data/three_tuples.txt','r',encoding='utf-8') as f:
    with open('three_tuples.txt','w',encoding='utf-8') as f2:
        for line in f.readlines():
            line=line.strip()
            line=line.split(':')
            try:
                f2.write('{}\t{}\t{}\n'.format(line[0],line[1],''.join(line[2:])))
            except:
                f2.write(''.join(line))
                
'''







