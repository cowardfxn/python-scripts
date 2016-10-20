from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

'''
sparkSQL试验
读取json格式的文本数据和整理数据结构
效率提升不明显
'''

conf = (SparkConf()
    .setMaster('local')
    .setAppName('lalala')
    .set('spark.executor.memory', '4g'))

sc = SparkContext(conf=conf)
ssql = SQLContext(sc)

path = 'file:///home/spark/sparktest/'
or1 = sc.textFile(path)
out_path = 'hdfs:///user/spark/DATA.json'
or1.saveAsTextFile(out_path)


path = '11_30s.json'
df1 = ssql.read.json(path)
df2 = df1.where('data <> null')
df2 = df2.toDF('duk', 'ct', 'data')
