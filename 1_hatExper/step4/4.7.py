# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
剔除掉杰青的author id，把剩下的co-author的 id 也按sortedName和affID合并

对剔除掉杰青author id后的author id的数据进行相同sortedName，affID合并操作

这里首先找到 co-author id 对应的名字sortedName

然后在
    r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\杰青论文id下的所有作者" \
    r"以及机构数据\filterCN_jqPaperID_authorID_affID.txt"
中把对应的affID找到

"""
import pandas as pd
import csv


def getSortedName(normalizedName):
    normalizedName = normalizedName.lower()
    names = normalizedName.split(' ')
    names.sort()
    return " ".join(names)


path1 = r"E:\FengXu\tmp\co_authorIDs.txt"
path2 = r"D:\Dataset\NEW_MAG\Authors.txt"
path3 = r"E:\FengXu\result1\coAuthorID_sortedName.txt"
co_authorIDs = set()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        co_authorIDs.add(line)
    pass
outer = open(path3, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[2] == "" or line[2] is None:
            continue
        if line[0] in co_authorIDs:
            sortedName = getSortedName(line[2])
            outer.write(line[0]+'\t'+sortedName+'\n')
    pass
outer.close()
