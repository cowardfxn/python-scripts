#!/usr/bin/python
# encoding: utf-8

'''
pyspark的sparkstreaming试验
接收socket传入的数据，统计词频后在终端输出结果
需要先启动socket server

'''


from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext


def proc():
    conf = (SparkConf()
        .setMaster("local[2]")
        .setAppName("streaming_test")
        .set("spark.driver.memory", "2g")
        .set("JAVA_HOME", "/usr/lib/jvm/java-7-oracle/jre/bin/java"))
    sc = SparkContext(conf=conf)
    sc.setLogLevel("WARN")

    ssc = StreamingContext(sc, 5)

    # updateStateByKey、reduceByKeyAndWindow 必须设置
    ssc.checkpoint("./")

    in_dstream = ssc.socketTextStream('localhost', 29999)
    # in_dstream = ssc.textFileStream('file:///mnt/share/codes') # 读取hdfs文件
    words = in_dstream.flatMap(lambda e: e.split(" ")).map(lambda x: (x, 1))
    
    # words = words.reduceByKey(lambda a, b: a + b)
    # words = words.updateStateByKey(updateState)

    # 第三个参数是windowDuration，设定的值必须是batchDuration的整数倍
    # 第四个参数是slideDuration，设定的值必须是batchDuration的整数倍
    # batchDuration就是StreamingContext初始化时设定的读取数据的时间间隔，这段代码里设置的是5(5000ms)
    words = words.reduceByKeyAndWindow(lambda a, b: a+b, lambda a, b: a-b, 10, 15)

    # 在log中打印结果
    words.pprint(27)
    ssc.start()
    ssc.awaitTermination()
    

def updateState(values, state):
    # print("type of values: {}".format(type(values)))
    # print("type of state: {}".format(type(state)))
    # values: list
    # state: None or int
    sum_val = 0
    if values:
        sum_val = sum(values)
    if state:
        sum_val += state
    return sum_val

if __name__ == '__main__':
    proc()
