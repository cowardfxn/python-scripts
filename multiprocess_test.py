#!/usr/bin/python
# encoding: utf-8

'''
multiprocessing模块测试

'''

import multiprocessing as multi
import os, time
from random import randint


def proc():
    pool = multi.Pool(processes=4)
    # res1 = pool.apply_async(os.getpid, ())
    # print res1.get(timeout=1)

    # multi_apply = [pool.apply_async(os.getpid, ()) for i in range(5)]
    # print [e.get(timeout=1) for e in multi_apply]

    map_res = pool.map_async(ft1, [range(4), range(6,9), range(12, 18)])
    print "map_async result: \n", map_res.get()

    map_res = pool.map(ft1, [range(4), range(6,9), range(12, 18)])
    print "\n\nmap result: ", map_res
    pool.close()

    pool.close()


def ft1(args):
    print "args: %s" % str(args)
    interval = randint(1, 10)
    print "Cur process ID: %s" % os.getpid()
    print "Sleep %ds..." % interval
    return ft2(interval)


def ft2(n):
    time.sleep(n)
    return n + 1


if __name__ == '__main__':
    proc()
