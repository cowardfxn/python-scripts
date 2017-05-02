#!/usr/bin/python
# encoding: utf-8
"""
多重绑定的装饰器
http://www.artima.com/weblogs/viewpost.jsp?thread=101605

使用方法:
from mm import multimethod

@multimethod(int, int)
def foo(a, b):
    return a * b - a

@multimethod(str, str)
def foo(a, b):
    return "{}, {}".format(a, b)

"""

registry = {}

class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}
    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)
    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function

# ver1 基础版本
def multimethod(*types):
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        return mm
    return register

# ver2 支持装饰器叠加
"""
@multimethod2(int, int)
@multimethod2(int)
def foo(a, b=10):
    return a * b - a

"""
def multimethod2(*types):
    def register(function):
        function = getattr(function, "__lastreg__", function) # 类似三目运算符，当装饰器叠加的情况时，获取的是被缓存的前一层装饰器
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm
    return register
