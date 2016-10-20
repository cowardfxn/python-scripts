#!/bin/env
# encoding: utf-8


'''
自动生成五环之歌
proc参数设定最高环数，然后依次递减输出

啊 五环 你比四环多一环
啊 五环 你比六环少一环
终于有一天 你会修到七环
修到七环怎么办
你比五环多两环'''

import random

f1 = '''啊 {0}环 你比{1[0]}环{1[1]}{1[2]}环
啊 {0}环 你比{2[0]}环{2[1]}{2[2]}环
终于有一天 你会修到{3[0]}环
修到{3[0]}环怎么办
你比{0}环{3[1]}{3[2]}环
'''

l1 = list(range(11))
l2 = list('零一二三四五六七八九十')
n2Chn = dict(zip(l1, l2))
n2Chs = lambda num: "".join([n2Chn[int(e)] for e in str(abs(num))])

def genSingleRing(n, direction, n_origin=0):
    p1 = random.randint(1, 3)
    line = []
    ring1 = n + direction * p1
    ring1_chs = n2Chs(ring1)
    if n_origin != 0:
        operator1 = (n_origin - ring1) > 0 and "少" or "多"
    else:
        operator1 = direction > 0 and "少" or "多"
    operand1_chs =  n2Chs(p1)
    
    return ring1, [ring1_chs, operator1, operand1_chs]

def proc(n):
    while n > 0:
        n_origin = n
        result = []
        result.append(n2Chs(n))

        _, single_ring = genSingleRing(n, 1)
        result.append(single_ring)
        _, single_ring = genSingleRing(n, -1)
        result.append(single_ring)
        n, single_ring = genSingleRing(n, -1, n)
        result.append(single_ring)

        # print result, "\n"
        print(f1.format(*result))


if __name__ == '__main__':
    proc(10)
