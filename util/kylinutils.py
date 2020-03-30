#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

import time
import requests
import sqlalchemy as sa
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def queryParse():
    kylin_engine = sa.create_engine('kylin://ADMIN:KYLIN@10.10.201.37:7070/demo?version=v1')
    results = kylin_engine.execute('SELECT DISTINCT(CBD_NAME) FROM STORE_INFO')
    for r in results:
        if(str(r[0]) != ""):
            sql = 'SELECT LA,LO FROM STORE_INFO where CBD_NAME =\'' + str(r[0]) + '\' limit 1'
            data = kylin_engine.execute(sql)
            for d in data:
                bdApi(str(r[0]), str(d[0]), str(d[1]))




# def query():
#     kylin_engine = sa.create_engine('kylin://ADMIN:KYLIN@10.10.201.37:7070/demo?version=v1')
#     results = kylin_engine.execute('SELECT DISTINCT(CBD_NAME),LA,LO FROM STORE_INFO')
#     i =0
#     for r in results:
#         if (i % 800 == 0):
#             time.sleep(5)
#         bdApi(str(r[0]),str(r[1]),str(r[2]))
#         i = i + 1


def bdApi(name,la,lo):
    url ="http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=" + la + "," + lo + "&output=json&pois=1&latest_admin=1&ak=nvzTa1X4SrxOAC8YA3XvFbDl2GBwlBVo"
    text = requests.get(url).text

    text = text.replace("renderReverse&&renderReverse(","")[:-1]

    data = json.loads(text)
    district = data["result"]["addressComponent"]["district"]
    print name +"\t"+ district

if __name__ == '__main__':
    # query()
    queryParse()

