#!/usr/bin/python
# encoding: utf-8

"""
启动命令: python nim_game.py [行数值 列数值]
参数说明:
    行数值 预期排列的行数
    列数值 预期每行的最大列数，最小列数的默认值是3
"""

import numpy as np
from itertools import permutations
from copy import copy
from sys import argv

# 返回安全的排列
# 玩家每一步操作后的棋局都能保证自己获胜
def nim_game_gen(max_row, max_col):
    result = []
    for assume_row in range(3, max_row+1):
        for pattern in permutations(np.arange(3, max_col+1), assume_row):
            if safe_composition(pattern):
                result.append(copy(pattern))
    return result

# 验证数组排列是否安全
def safe_composition(in_list):
    in_array = np.array(in_list, dtype=np.uint8).reshape(-1, 1)
    bin_matrix = np.unpackbits(in_array, axis=1)
    sum_vals = np.sum(bin_matrix, axis=0)
    # np.all(sum_vals == 0 or (sum_vals > 1 and sum_vals % 2 == 0))

    safe_ptr = True
    for v in sum_vals:
        if v == 1 or v % 2 != 0:
            safe_ptr = False
            break
    return safe_ptr

if __name__ == '__main__':
    if len(argv) != 3:
        row_num, col_num = 3, 6
        print("无效的参数输入，使用默认设置 行数: {}, 列数: {}".format(row_num, col_num))
    else:
        row_num, col_num = argv[1:]

    l1 = nim_game_gen(int(row_num), int(col_num))
    if l1:
        for e in l1:
            print(str(e))
    else:
        print("未发现安全的排列数字组合，不考虑改变行列数吗？")

