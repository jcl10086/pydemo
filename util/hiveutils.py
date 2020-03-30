#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from pyhive import hive
from TCLIService.ttypes import TOperationState


if __name__ == '__main__':
    cursor = hive.connect(host="master", port="10000", username="admin").cursor()
    cursor.execute("select * from store_info limit 1")