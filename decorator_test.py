#!/usr/bin/python
# _*_ encoding: utf-8 _*_

'''
装饰器原理验证
'''

from random import random

def decorator1(func1):
    def wrapper(*s_args):
        print "decorator1 starts..."
        print "arg1:", func1(*s_args)
        print "decorator1 ends..."
    return wrapper

def decorator2(arg2):
    print "decorator2 starts..."
    print "arg2:", arg2(random)
    print "decorator2 ends..."
    return decorator2

def decorator3(arg3):
    print "decorator3 starts..."
    print "arg3:", arg3(random)
    print "decorator3 ends..."
    return arg3

@decorator3
@decorator2
@decorator1
def proc():
    res = []
    print "Main proc..."
    for e in xrange(1000):
        if e % 55 == 0:
            res.append(e)
    print "Main proc ends..."
    return res

if __name__ == '__main__':
    proc()
