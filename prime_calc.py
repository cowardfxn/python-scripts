#!/usr/bin/python
# encoding: utf-8

'''
新奇的质数计算方法

'''

import sys

def sieve(n):
    x = [1] * n
    x[1] = 0
    for i in range(2, n/2):
        j = 2 * i
        while j <  n:
            x[j] = 0
            j = j + i
    return x

def prime(n, x):
    i = 1
    j = 1
    while j <= n:
        if x[i] == 1:
            j += 1
        i += 1
    return i - 1

if __name__ == '__main__':
    x = sieve(10000)
    code = [1206, 301, 384, 5]
    key = [1, 1, 2, 2]
    # print("".join(chr(i) for i in [73, 83, 66, 78, 32, 61, 22]))
    sys.stdout.write("".join(chr(i) for i in [73, 83, 66, 78, 32, 61, 22]))

    cont = ""
    for i in range(0, 4):
        # cont += str(prime(code[i], x) - key[i])
        sys.stdout.write(str(prime(code[i], x) - key[i]))
    # print(cont)

'''
http://python.jobbole.com/86496/

def sieve(n):             //对n以内的数进行筛选，返回一个长度为n的布尔数组
    #compute primes using sieve eratosthenes
    x = [1] * n         //定义长度为n的布尔数组（实际上电影里用1和0来表示true和false了）
    x[1] = 0            //1既不是素数也不是合数，设为0

    for i in range(2,n/2)://i从2开始一直到n/2
        j = 2 * i    //j从2倍i开始
        while j < n:
            x[j] = 0  //把所有i的倍数筛除
            j = j + i //下一个i的倍数
    return x          //返回数组

def prime(n,x):   //求第n个素数，只需要在筛选好的布尔数组中找第n个标记为1的数就可以了
    #Find nth prime
    i = 1    //初始化为1
    j = 1
    while j <= n:   //在布尔数组中寻找第n个标记为1的数
        if x[i] == 1:
            j = j + 1
        i = i + 1
    return i-1    //前面循环中i多加了一次，返回时需要减1
'''
