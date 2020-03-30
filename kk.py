#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime
import pymysql

if __name__ == '__main__':
    db = pymysql.connect("localhost", "root", "123", "test", charset='utf8')
    cursor = db.cursor()
    starttime = datetime.datetime.now()
    cursor.execute("select * from store_info")
    array = []
    for tuple in cursor.description:
        array[tuple]
    endtime = datetime.datetime.now()
    print "运行次数：" + array + "====" + "运行时间:" + str((endtime - starttime).seconds)
    cursor.close()
    db.close()