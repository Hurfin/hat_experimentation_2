# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd
import numpy as np

path1 = r"E:\FengXu\result\TMP\paperID_authorID_affiliationID_paperYear_firstPaperYear(Co).txt"
path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
path3 = r"D:\Dataset\NEW_MAG\Papers.txt"
pathOut = r"E:\FengXu\result\TMP\paperID_authorID_paperYear(coPaperALL).txt"
coAuthorIDs = set()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        coAuthorIDs.add(line[1])
    pass
index_ = {}  # 记录某个paper id都在哪些行(记录索引值)
ans_ = []
ans_APPEND = ans_.append
cnt = 0
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in coAuthorIDs:  # 如果作者在这个co author集合里，就保留
            ans_APPEND([line[0], line[1]])  # 存paper id, author id
            if line[0] not in index_.keys():
                index_[line[0]] = []
            index_[line[0]].append(cnt)
            cnt += 1
            pass
    pass
del coAuthorIDs
with open(path3, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[7] == '' or line[7] is None:  # paper year为空则pass
            continue
        if float(line[7]) < 1989:  # paper year 小于1989的去掉
            continue
        if line[0] in index_.keys():  # 如果有这个论文
            paper_index = index_[line[0]]  # 拿到它所在的所有行号
            for index_i in paper_index:  # 对每个paper id所在行末尾添加上年份
                ans_[index_i].append(line[7])
    pass
cnt = 0
with open(pathOut, 'w', encoding='utf-8') as f:
    for row_i in ans_:
        if len(row_i) != 3:
            cnt += 1
            continue
        f.write('\t'.join(row_i)+'\n')
    pass
print('multi year rows', cnt)
# 236564