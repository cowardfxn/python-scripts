#!/usr/bin/python
# _*_ encoding: utf-8 _*_

'''
身份证号码有效性验证

'''

def ID_valid(instr):
    in_nums = [int(e) for e in instr[:-1]]
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    multi_rslt = [in_nums[i] * weights[i] for i in range(len(in_nums))]
    last_num = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    return last_num[sum(multi_rslt) % 11]

# 大量验证时，可采用numpy使用矩阵乘法验证

if __name__ == '__main__':
    print ID_valid('34052419800101001X')
