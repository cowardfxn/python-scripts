#!/usr/bin/python
# encoding: utf-8

'''
多重排序功能实现

'''

d1 = {1:23, 'b': 62}
d2 = {1:24, 'b': 2}
d3 = {1:23, 'b': 54}
d4 = {1:23, 'b': 1}
d5 = {1:01, 'b': 9}
d6 = {1:23, 'b': 32}
d7 = {1:05, 'b': 33}
d8 = {1:39, 'b': 100}

li = [d1, d2, d3, d4, d5, d6, d7, d8]

def cmpf(a, b, key1, key2):
     if (a[key1] != b[key1]):
             return a[key1] - b[key1]
     else:
             return a[key2] - b[key2]

def rcmpf(a, b, key1, key2):
     if (a[key1] != b[key1]):
             return b[key1] - a[key1]
     else:
             return a[key2] - b[key2]

rslt = sorted(li, cmp=lambda a,b: cmpf(a, b, 1, 'b'))
sorted(li, cmp=lambda a,b: rcmpf(a, b, 1, 'b'))
