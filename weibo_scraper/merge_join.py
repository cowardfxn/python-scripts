#!/usr/bin/python
# encoding: utf-8
# Author: fanxn
# Date: 2018/4/23

import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'key': ['K1', 'K2', 'K3', 'K4'],
    'A': ['A1', 'A2', 'A3', 'A8'],
    'B': ['B1', 'B2', 'B3', 'B8']
})

df2 = pd.DataFrame({
    'key': ['K3', 'K4', 'K5', 'K6'],
    'A': ['A3', 'A4', 'A5', 'A6'],
    'B': ['B3', 'B4', 'B5', 'B6']
})

print('df1=\n{}\n'.format(df1))
print('df2=\n{}\n'.format(df2))

merge_df = pd.merge(df1, df2)
merge_inner_on_key = pd.merge(df1, df2, how='inner', on=['key'])
merge_left = pd.merge(df1, df2, how='left', suffixes=('_l', '_r'))
merge_left_on_key = pd.merge(df1, df2, how='left', on=['key'])
merge_right = pd.merge(df1, df2, how='right')
merge_right_on_key = pd.merge(df1, df2, how='right', on=['key'])
merge_outer = pd.merge(df1, df2, how='outer', on=['key'])

print('merge_df=\n{}\n'.format(merge_df))
print('merge_inner_on_key=\n{}\n'.format(merge_inner_on_key))
print('merge_left=\n{}\n'.format(merge_left))
print('merge_left_on_key=\n{}\n'.format(merge_left_on_key))
print('merge_right=\n{}\n'.format(merge_right))
print('merge_right_on_key=\n{}\n'.format(merge_right_on_key))
print('merge_outer=\n{}\n'.format(merge_outer))