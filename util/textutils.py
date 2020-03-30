#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime
import random

#随机生成时间
import time


def randomtimes():
    a1 = (2000, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2018, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）

    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳

    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    return date



def prodata(start, end):
    names = ['a','b','c','d','e','f','g','h','i','j','k']
    for i in range(start,end):
        id = str(i)
        name = random.choice(names)
        age = str(random.randint(10,70))
        time = randomtimes()
        # print time
        f = file("/opt/aa.txt", "a+")
        f.write(id + '\t' + name + '\t' + age + '\t' + time)
        f.write('\n')

if __name__ == '__main__':
    prodata(1, 21)