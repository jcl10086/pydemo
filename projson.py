#!/usr/bin/env python 
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('d:/zz.txt', 'r') as f:
        list = f.readline().split('\t')
        # list = f.read().split('\t')
        map(list[0],list[1])
        print(f.read())