#!/usr/bin/python
#encoding=utf-8

'''
matplotlib使用

'''

import numpy as np
from matplotlib import pyplot as plt

# 三次方程
def func1(n=10000):
    x = np.array(range(n))
    # x + x^2 + x^3
    y = np.array([e + e**2 + e**3 for e in x])
    plt.title('三次方程')
    plt.plot(x, y)
    plt.show()

# 二次方程
def func2(n=10000):
    x = np.array(range(n))
    # n + x + x^2
    y = np.array([n + e + e**2 + e**3 for e in x])
    plt.plot(x, y)
    plt.show()



if __name__ == '__main__':
    func1(10**10)
    func2(10**10)

