# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
将杰青按领域分类
（将sortedName为中文名的剔除掉）
"""
import numpy as np
import pandas as pd
import os
import csv
path0 = r'E:\pythonCode\RJ_experimentation_1\Data\field\affiliationID_sortedName_fatherFieldID_fieldName.txt'
path1 = r'E:\pythonCode\RJ_experimentation_1\Data\field\fields.txt'


def checkChinese(sortedName):
    for ch in sortedName:
        if not ('a' <= ch <= 'z' or ch == ' '):
            return True
    return False


fields = []
with open(path1, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        fields.append(line)

JQs = []
with open(path0, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        if checkChinese(line[1]) == True:
            continue
        JQs.append(line)

print(fields[0])
print(JQs[0])

# 每个领域建立一个映射
field_dict = dict()
for field in fields:
    key_i = (field[0], field[1])
    field_dict[key_i] = set()

for jq in JQs:
    key_i = (jq[2], jq[3])
    if key_i in field_dict.keys():
        field_dict[key_i].add((jq[0], jq[1]))
    else:
        print('没有该领域')

# 检查各领域杰青间有没有重叠
# for i in range(0, len(fields)-1):
#     for j in range(i+1, len(fields)):
#         key_i = (fields[i][0], fields[i][1])
#         key_j = (fields[j][0], fields[j][1])
#         print(key_i, key_j, len(field_dict[key_i]&field_dict[key_j]))
#         pass
#     pass

# 经过讨论把领域内杰青数目小于等于2的领域排除省略掉
for k, v in field_dict.items():
    print(k, len(v))
    path_i = 'E:/pythonCode/RJ_experimentation_1/Data_1/field_jq/' + str(k[0]) + "_" + str(k[1]) + ".txt"
    if len(v) <= 2:
        continue
    with open(path_i, 'w', encoding='utf-8') as f:
        for st in v:
            f.write(st[0]+'\t'+st[1]+'\n')

# fieldsName = [name[1] for name in fields]
