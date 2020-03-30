#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime
import requests
import pymysql
import json
import decimal

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def kk():
    db = pymysql.connect("localhost", "root", "123", "copy-fugong", charset='utf8')
    cursor = db.cursor()
    cursor.execute("select id,depart_name from area where parent_id = ''")
    datas = cursor.fetchall()
    for data in datas:
        sql1 = "select id,depart_name from area where parent_id = '" + data[0] + "'"
        cursor.execute(sql1)
        datas1 = cursor.fetchall()
        for data1 in datas1:
            sql2 = "select id,depart_name from area where parent_id = '" + data1[0] + "'"
            cursor.execute(sql2)
            datas2 = cursor.fetchall()
            for data2 in datas2:
                print data[1] + " " + data1[1] + " " + data2[1]
                s = ts(data[1] + data1[1] + data2[1])
                strs = s.split("_")
                sql3 = "insert into area_info(province,city,district,lo,la,area_id) values('" + data[1] +"','" + data1[1] +"','" + data2[1] +"','" + strs[0] +"','" + strs[1] +"','" + data2[0] +"')"
                cursor.execute(sql3)
    db.commit()
    cursor.close()
    db.close()

def ts(addr):
    url = "http://api.map.baidu.com/geocoding/v3/?address=" + addr + "&output=json&ak=rCTy5lCj9ZWNdnocAqSAsXfB5T00gqVh"
    text = requests.get(url).text
    data = json.loads(text)
    da = data["result"]["location"]
    s = str(da['lng']) + "_"  + str(da['lat'])
    return s

if __name__ == '__main__':
    kk()