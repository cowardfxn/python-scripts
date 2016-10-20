#!/user/bin/python
# encoding: utf-8

'''
不使用random模块生成随机数
算法还是有被破解的可能，不够完备

'''

import time
class RD(object):
    def __init__(self, seed=1.1):
        self.seed = seed
        self.value = self.seed * time.time() % 1
    def next(self):
        self.value = (self.value * 10 + self.seed) % self.value
        while self.value < 0.1:
            self.value = self.value * 10
        return self.value
LEN = 6
rd = RD()
print(sum([int(rd.next() * (10 ** i)) for i in range(LEN+1)]))
