#!/usr/bin/python
# encoding: utf-8
# Author: fanxn
# Date: 2017/2/22


'''
相邻数据去重，不相邻的则保留不动
'''

from copy import copy
import numpy as np


# 循环遍历版本，接收iterable参数
# 返回值类型为list
def wipe_duplication(input_list):
    if len(input_list) < 2:
        return input_list
    result = []
    prv_val = ""
    for prn_val in input_list:
        if prn_val != prv_val:
            result.append(copy(prn_val))
            prv_val = prn_val
    return result


# numpy版本，参数为(1, n)的numpy数组
# 返回值同样为numpy数组
def dupli_wipe(input_array):
    diff = np.diff(input_array)
    # 第一列数据需要保留
    diff = np.hstack((1, diff))
    diff_idx = np.where(diff != 0)
    wiped_array = input_array[diff_idx]
    return wiped_array


# 测试函数
def test():
    a1 = np.random.random_integers(1, 3, 20)
    r1 = wipe_duplication(a1)
    r2 = dupli_wipe(a1).tolist()

    return r1 == r2, a1.tolist()


if __name__ == "__main__":
    test_rslt = []
    debug = []
    for i in range(100000):
        run_result, sample_array = test()
        if not run_result:
            debug.append(sample_array)
        test_rslt.append(run_result)
    # print(test_rslt)
    print("All tests ran correctly: {}".format(all(test_rslt)))
    if debug:
        print(debug)
