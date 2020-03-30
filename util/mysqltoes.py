#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName('') \
        .getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')

    # data = spark.createDataFrame([(1,2), (3,4)], ('a', 'b'))
    # data = data.withColumn('c', addCol(data['a']))
    # # data.show()
    # data = data.write.format('hive').mode('append').saveAsTable('test')
    # # data = data.write.saveAsTable('hdfs://10.10.201.37:8020/warehouse/tablespace/external/hive/test', mode='overwrite')
    columns = ['id','store_name']
    mysqlData = spark.read.format("jdbc")\
        .option("driver", "com.mysql.jdbc.Driver") \
        .option("url", "jdbc:mysql://10.10.201.31:3306/demo") \
        .option("dbtable", "store_info_sb") \
        .option("user", "root") \
        .option("password", "jr&0ZmuZ@rmp^H&") \
        .load()

    mysqlData = mysqlData.selectExpr(
        "id",
        "store_name",
        "cook_class",
        "per_consumption",
        "lo",
        "la",
        "province",
        "city",
        "avt_rate",
        "feedback_count",
        "taste_rate",
        "env_rate",
        "service_rate",
        "cbd_name",
        "store_name_full",
        "store_address",
        "regexp_replace(from_unixtime(unix_timestamp(created_time, 'yyyy-MM-dd HH:mm:ss'), 'yyyy-MM-dd HH:mm:ss'),' ','T') as created_time",
        "url",
        "branch",
        "city_id",
        "sales",
        "regexp_replace(from_unixtime(unix_timestamp(opening_date, 'yyyy-MM-dd'), 'yyyy-MM-dd'),' ','T') as opening_date"
        )
    mysqlData.show()

    # mysqlData.write.format('org.elasticsearch.spark.sql').option('es.nodes', '10.10.201.31').option('es.port', '9200') \
    #     .option('es.resource', 'store_info_s/nested_type') \
    #     .option('es.mapping.id', 'id') \
    #     .save(mode='append')