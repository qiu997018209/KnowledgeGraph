环境:python3+flask+mysql+D3

1.data:数据处理
	(1)data.py将爬虫趴下来的html数据处理成三元组，存在文件:three_tuples.txt
	(2)mysql.py将three_tuples.txt里数据存入Mysql数据

2.visualization:可视化
	(1)执行run_server.py，启动web服务，然后在浏览器中输入:
	http://192.168.1.245:8090/api/v1?car_name=日产天籁
	(2)原理:flask框架下查询mysql，存入json文件，index.html导入json文件，采用用D3的js框架
	(3)效果见:效果.PNG
	(4)数据量:11200个
3.conf.py:配置文件