#!/usr/bin/python
# encoding: utf-8

'''
datetime转换
'''

from datetime import datetime
def calc(d):
    if d < 100:
        return "Invalid number!"
    else:
        for i in xrange(100, d):
            str_d = list(str(i))
            n = len(str_d)
            r = 0
            for d in str_d:
                r += int(d) ** n
            if r == i:
                print i

s = datetime.now()
calc(100000000)
e = datetime.now()
print (e-s).total_seconds()
