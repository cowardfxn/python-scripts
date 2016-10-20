#!/usr/bin/python
# encoding: utf-8

'''
递归实现power函数

'''

def power(x, n):
    if n > 0:
        if n % 2 == 0:
            return power(x, n / 2) ** 2
        else:
            return x * power(x, n - 1)
    elif n == 0:
        return 1
    else:
        return 1 / power(x, -n)


if __name__ == '__main__':
    print power(3, 3)
    print power(6, 6)
    print power(9, 19)
