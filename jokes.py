#!/bin/env
# encoding: utf-8

'''
玩笑
无限循环
'''

from sys import maxint

def tellStory(cnt):
    rtn_str = ''
    rtn_str += "从前有座山\n"
    rtn_str += "山上有座庙\n"
    rtn_str += "庙里有个老和尚和一个小和尚\n"
    rtn_str += "有一天\n"
    rtn_str += "小和尚对老和尚说\n"
    rtn_str += "\"给我讲个故事吧\"\n"
    rtn_str += "于是, 老和尚说: \n"
    rtn_str += "-----------\n在%s年前\n" % cnt
    yield rtn_str

if __name__ == '__main__':
    for i in xrange(1, maxint, 2):
        for e in tellStory(i):
            print e
