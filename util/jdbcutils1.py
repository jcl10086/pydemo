#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime

import pymysql
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

db = pymysql.connect("master", "root", "Sugon@123", "cboard-demo",  charset='utf8')
cursor = db.cursor()

cursor.execute("select store_name,cook_class,province,city,cbd_name,id from store_info limit 10")
datas = cursor.fetchall()
mothons = ['01','02','03','04','05','06','07','08','09','10','11','12']
for data in datas:
    try:
        for num in mothons:
            sql = "INSERT INTO store_info_sales_monthly(store_name,cook_class,province,city,cbd_name,sales,cost,month,year,sid) VALUES('" + data[
                0] + "','"+data[1]+"','"+data[2]+"','"+data[3]+"','"+data[4]+"',(50000+RAND()*40000),(50000+RAND()*40000)*0.8," \
                     "'" + num + "','2018','"+str(data[5])+"')"
            cursor.execute(sql)
    except:
        print "数据异常"
    print "===="+data[0]
    db.commit()
cursor.close()
db.close()