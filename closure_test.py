#!/usr/bin/python
# _*_ encoding: utf-8 _*_

'''
闭包原理验证
'''

def makeConstantAdder(X):
    constant = X
    def adder(x):
        return x + X
    return adder

if __name__ == '__main__':
    f = makeConstantAdder(12)
    print f(1)
    print f(3)
    g = makeConstantAdder(5)
    print g(0)
    print g(4)
