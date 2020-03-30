#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
import aa


SparkContext.setSystemProperty('hive.metastore.uris', 'thrift://10.10.201.37:9083')

@udf(returnType=StringType())
def addCol(a):
    data = aa.bdApi(35 + a, 120 + a)
    return data

if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName('') \
        .master('local') \
        .enableHiveSupport() \
        .getOrCreate()
    spark.sparkContext.setLogLevel('INFO')

    data = spark.createDataFrame([(1,2), (3,4)], ('a', 'b'))
    data = data.withColumn('c', addCol(data['a']))
    # data.show()
    data = data.write.format('hive').mode('append').saveAsTable('test')
    # data = data.write.saveAsTable('hdfs://10.10.201.37:8020/warehouse/tablespace/external/hive/test', mode='overwrite')
