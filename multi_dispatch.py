#!/usr/bin/python
# encoding: utf-8
# Author: fanxn
# Date: 2017/5/5


"""
用于多重绑定的装饰器，根据使用装饰器时传入的参数定义使用哪个函数
类似多个if..elif分支，但是没有全局默认的else选项
由于装饰器函数的参数需要作为全局字典registry的key，因此必须是hashable的
可以用于同时装饰多个函数的多个分支
使用场景有限，性能一般
参考资料: http://www.artima.com/weblogs/viewpost.jsp?thread=101605
"""

registry = {}


class MultiDispatch(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args):
        if len(args) == 0:
            raise TypeError("Invalid registry")
        types = args[0]
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)

    def register(self, types, function):
        if len(types) == 0:
            raise TypeError("Invalid registry")
        types = types[0]
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function


def multi_dispatch(*types):
    def register(function):
        function = getattr(function, "__lastreg__", function)  # 类似三目运算符，当装饰器叠加的情况时，获取的是被缓存的前一层装饰器
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiDispatch(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm

    return register


@multi_dispatch("hey")
def f1(a, b):
    print("first parameter is hey")
    print("second parameter is {}".format(b))


@multi_dispatch(1)
def f1(a, b):
    print("a: {}".format(a))
    print("b: {}".format(b))


if __name__ == '__main__':
    f1("hey", 3)
    try:
        f1(4, 5)
    except Exception as e:
        print(e)
    f1(1, 2)
