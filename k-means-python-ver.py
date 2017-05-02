#!/usr/bin/python
# encoding: utf-8

"""
http://blog.csdn.net/zouxy09/article/details/17589329
"""

import numpy as np
import time
import matplotlib.pyplot as plt

# 计算欧氏距离
def euclDistance(vector1, vector2):
    return np.sqrt(np.sum(np.power(vector2 - vector1, 2)))

# 初始化质心随机样本
def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = np.zeros((k, dim))
    for i in range(k):
        index = int(np.random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]  # 随机取dataSet中的某个样本(即一行数据)为质心
    return centroids

# k-means 聚类
def kmeans(dataSet, k):
    numSamples = len(dataSet)
    clusterAssment = np.mat(np.zeros((numSamples, 2)))  # 作用类似KMeans返回对象的clf.labels_
    clusterChanged = True
    centroids = initCentroids(dataSet, k)
    while clusterChanged:
        clusterChanged = False
        for i in xrange(numSamples):  # 对于每一个样本
            minDist = np.maximum  # 质心距离阈值，设定一个极大值
            minIndex = 0
            for j in range(k):  # 对每一个与设定的聚类质心
                distance = euclDistance(centroids[j, :], dataSet[i, :])  # 求初始质心和样本的距离
                if distance < minDist:  # 如果样本与质心距离小于预设最大阈值
                    minDist = distance  # 更新最大距离
                    minIndex = j

            if clusterAssment[i, 0] != minIndex:  # 如果当前样本与质心的距离小于已知最小距离
                clusterChanged = True  # 设置质心有更新，因此样本需要重新计算
                clusterAssment[i, :] = minIndex, minDist**2  # 记录下当前样本的index和与质心的距离
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]]  # 取与质心距离在设定阈值内的样本
            centroids[j, :] = np.mean(pointsInCluster, axis=0)  # 计算范围内样本平均值，作为更新后的质心位置
    print("cluster completed!")
    return centroids, clusterAssment  # 循环结束后，返回质心位置和每个样本所在的质心


# 暂时只能绘制二维图形
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print("Sorry! Dimension is beyond 2")
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1
 
    # 画出所有样例点 属于同一分类的绘制同样的颜色
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
 
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb'] #设定颜色
 
    # draw the centroids
    # 画出质点，用特殊图型
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
 
    plt.show()

if __name__ == '__main__':
    print("step 1: load data...")
    dataSet = []
    with open("./data.txt") as ifs:
        for line in ifs:
            line = line.strip().split(" ")
            dataSet.append((float(line[0]), float(line[1])))
    print("step 2: clustering")
    dataSet = np.mat(dataSet)

    k = 4
    centroids, clusterAssment = kmeans(dataSet, k)

    print("step 3: show the result...")
    showCluster(dataSet, k, centroids, clusterAssment)
