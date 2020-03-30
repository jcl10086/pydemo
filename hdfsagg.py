#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from hdfs.client import Client

def read_hdfs_file(client, path):
    lines = []
    with client.read(path, encoding='utf-8') as reader:
        for line in reader:
            lines.append(line)
    return lines

# 追加数据到hdfs文件
def append_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=False, append=True, encoding='utf-8')

def mkdirs(client, hdfs_path):
    client.makedirs(hdfs_path)

# 覆盖数据写到hdfs文件
def create_to_hdfs(client, hdfs_path):
    client.write(hdfs_path, "", encoding='utf-8')

def list(client,hdfs_path):
    return client.list(hdfs_path, status=False)

if __name__ == '__main__':
    client = Client("http://10.0.13.190:50070")
    hdfs_path = "/warehouse/tablespace/external/hive/store_info_orc"
    list = list(client, hdfs_path)

    for filename in list:
        path = hdfs_path + "/" + filename
        data = read_hdfs_file(client, path)
    # data = read_hdfs_file(client)
    # create_to_hdfs(client, "/file/1.txt")
    # append_to_hdfs(client, "/file/1.txt", data)