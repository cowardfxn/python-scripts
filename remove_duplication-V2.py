#!/usr/bin/python
# encoding: utf-8

import numpy as np

"""
numpy数组去重
二维数组版本，需要指定去重使用的数据列

"""

# 二维数组版本，根据指定列去重，使用numpy自带方法
def wipe_dupl(input_array, axis_idx):
    diff = np.diff(input_array, axis=0)
    diff = np.vstack((np.ones(input_array.shape[1]), diff))
    diff_idx = np.where(diff[:, axis_idx] != 0)
    rslt = input_array[diff_idx]
    return rslt

# 二维数组版本，根据指定列去重，手动遍历
def dupl2(input_array, axis_idx=""):
    rslt = [input_array[0]]
    val0 = input_array[0][axis_idx]
    for row in input_array[1:]:
        val1 = row[axis_idx]
        if val0 != val1:
            rslt.append(row)
            val0 = val1
    return np.array(rslt)

def test_matrix():
    diffs = []
    for i in range(1000000):
        a1 = np.random.randint(1, 5, (10, 10))
        idx = np.random.randint(10)
        r1 = wipe_dupl(a1, idx)
        r2 = dupl2(a1, idx)
        if not np.all(r1 == r2):
            diffs.append((a1, idx))
    return diffs

if __name__ == '__main__':
    diffs = test_matrix()
    if diffs:
        print(diffs[0][0])
        print("")
        pritn(diffs[0][1])
    else:
        print("All passed!")
