# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
检查之前的数据中哪些杰青可以用，几个数据集的杰青的交集如何
"""
import pandas as pd
import os

path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\field\affID_sortedName_fieldID_fieldName.txt"

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveJIFPerYear(before5ANDafter5).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_h-IndexPerYear(before5ANDafter5).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_paperCntPerYear(Before5ANDafter5).txt"

_all_need_JQ = set()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        _all_need_JQ.add((line[0], line[1]))

_jif_JQ = set()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        _jif_JQ.add((line[0], line[1]))

_hIndex_JQ = set()
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        _hIndex_JQ.add((line[0], line[1]))

_paperCnt_JQ = set()
with open(path3, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        _paperCnt_JQ.add((line[0], line[1]))

print(len(_all_need_JQ), len(_jif_JQ), len(_hIndex_JQ), len(_paperCnt_JQ))
print(len(_all_need_JQ&_jif_JQ), len(_all_need_JQ&_hIndex_JQ), len(_all_need_JQ&_paperCnt_JQ))
