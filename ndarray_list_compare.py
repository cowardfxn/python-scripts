#!/usr/bin/env
# encoding: utf-8

'''
使用np.ndarray和list存储数据，
过滤数据性能比较

'''

from datetime import datetime, timedelta
import numpy as np
from timeit import timeit

def data_gen(n):
    total = n * 10000
    time_delta = timedelta(seconds=1)
    time_stamp = datetime.max
    result = []
    for i in xrange(total):
        time_stamp = time_stamp - time_delta
        result.append([time_stamp.strftime("%Y/%m/%d %H:%M:%S"), 2 * i, i ** 2, i+2])
    return result

def access_with_ndarray(data):
    c3 = np.array(data[:, -1], dtype=np.float32)
    c3 = (c3 > 1) & (c3 % 2 == 0)
    c3 = np.where(c3)
    return data[c3[0], :]

def default_iterate(data):
    rslt = []
    for e in data:
        i = e[-1]
        if i > 1 and i % 2 == 0:
            rslt.append(e)
    return rslt


if __name__ == '__main__':
    data = data_gen(50)
    np_data = np.array(data)

    a1 = []
    print "Direct access:"
    t1 = timeit(stmt=lambda: data[4500:40000], number=10)
    print "Access with default list slice: %e" % t1
    t2 = timeit(stmt=lambda: np_data[4500:40000, :], number=10)
    print "Access with structure ndarray: %e" % t2
    print "\n" + "==" * 12 + "\n"

    t3 = timeit(stmt=lambda: default_iterate(data), number=10)
    print "Access with default list iterating: %e" % t3
    t4 = timeit(stmt=lambda: access_with_ndarray(np_data), number=10)
    print "Access with default ndarray filtering: %e" % t4

