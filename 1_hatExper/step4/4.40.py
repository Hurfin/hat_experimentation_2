# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找dz.txt中fxID对应的领域
从杰青合作者中查找有没有合作关系，有合作关系就分到该杰青的领域

已有fxID和coAuthorID的对应关系（由于之前的筛选，它们的对应关系是一对一的）
需要找到fxID、coAuthorID、jqPaperID 然后是找到jqID和对应的领域信息

得到E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\coAuthorID_fxID_jqPaperIDs.txt
"""
import pandas as pd
path0 = r"E:\FengXu\tmp\1_fxID_coAuthorID.txt"
# path1 = r"E:\FengXu\result2\jqPaperID_coAuthorID_affID.txt"
path1 = r"E:\FengXu\result1\jqPaperID_authorID_affID.txt"
# check下
coAuthorID_fxID_dict = dict()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] not in coAuthorID_fxID_dict.keys():
            coAuthorID_fxID_dict[line[1]] = []
        coAuthorID_fxID_dict[line[1]].append(line[0])

for k, v in coAuthorID_fxID_dict.items():
    coAuthorID_fxID_dict[k] = list(set(v))

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in coAuthorID_fxID_dict.keys():
            coAuthorID_fxID_dict[line[1]].append(line[0])

cnt = 0
cntt = 0
path_out = r"E:\FengXu\result2\coAuthorID_fxID_jqPaperIDs.txt"
with open(path_out, 'w', encoding='utf-8') as f:
    for k, v in coAuthorID_fxID_dict.items():
        if len(v) > 2:
            cnt += 1
        if len(v) == 1:
            cntt += 1
        f.write(k+'\t'+'\t'.join(v)+'\n')
f.close()
print(cnt)
print(cntt)
# 有573个coAuthor有多篇杰青的论文
