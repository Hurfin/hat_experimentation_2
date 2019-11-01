# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
上一个程序把co-author合并了(同authorID,同name为同一个人. 同affID, 同name为同一个人)

现在考虑用之前讨论的方式去筛选(即:
1. 找杰青们的first year的min和max，当作筛选条件1（上一个程序已经找过了）
min max为1980 2007
2016太晚了，发现对有些杰青，数据集里只有他获奖后的论文，获奖前没有论文，（要把这些杰青删掉）

2. 用 学术年龄>=10 作为条件筛选，学术年龄用co-author的 last paper year 减去 first paper year
对co-author用这个条件筛选的话，对杰青也应该这样筛选下（保留last paper year - first paper year >= 10的杰青，大概还剩929人）
)

这里先找 co-author 的 first paper year 和 last paper year
"""
import pandas as pd

path1 = r"E:\FengXu\tmp\fxID_affID_sortedName_coAuthorID(drop_multi_CoAuthorID).txt"
path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
path3 = r"D:\Dataset\NEW_MAG\Papers.txt"

# data = pd.read_csv(path1, sep='\t')
# 找coAuthor的first paper year和last paper year
coAuthorID_sets = set()
bool_ = True
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if bool_ is True:
            bool_ = False
            continue
        coAuthorID_sets.add(line[3])
    pass

path_out1 = r"E:\FengXu\result1\paperID_coAuthorID.txt"
outer1 = open(path_out1, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in coAuthorID_sets:
            outer1.write(line[0]+'\t'+line[1]+'\n')
    pass
outer1.close()

