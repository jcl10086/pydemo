#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime

import pymysql

db = pymysql.connect("master", "root", "Sugon@123", "cboard-demo", charset='utf8')
cursor = db.cursor()
for i in range(1,20):
    starttime = datetime.datetime.now()
    cursor.execute(
        "insert into store_info(store_name,cook_class,per_consumption,lo,la,province,city,avt_rate,feedback_count,taste_rate,env_rate,service_rate,cbd_name,store_name_full,store_address,url,branch,city_id,sales,la_lo)"
        "SELECT * from ( "
        "select CONCAT(t1.store_name,cast(floor(rand()*100)+1 as char)) as store_name,t1.cook_class,t1.per_consumption,t1.lo+0.001 as lo,t1.la+0.001 as la,t1.province,t1.city,t1.avt_rate, t1.feedback_count,t1.taste_rate, t1.env_rate,t1.service_rate,t1.cbd_name,CONCAT(t1.store_name_full,cast(floor(rand()*100)+1 as char)) as store_name_full,t1.store_address,t1.url,t1.branch, t1.city_id,t1.sales+150.5 as sales,t1.la_lo  from store_info as t1  join  (select round(RAND() * ((select MAX(id) "
        "from store_info) - (select MIN(id) from store_info)) + (select MIN(id) from store_info)) as id) as t2  where t1.id >=t2.id and t1.lo <> '' and la <> '' ORDER BY t1.id limit 10000000"
        " ) a")
    endtime = datetime.datetime.now()
    print "运行次数：" + str(i) + "====" + "运行时间:" + str((endtime - starttime).seconds)

cursor.close()
db.close()