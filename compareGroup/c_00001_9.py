# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\Jieqing_minPaperYear_authorCnt.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\TMP\firstYear_authorCnt.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_" \
        r"paperYear_firstPaperYear(Co).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthor_age5_25_Aff_CN_paperNum5more.txt"

data1 = pd.read_csv(path3, sep='\t', header=None, names=['authorID'])
data2 = pd.read_csv(path2, sep='\t', header=None,
                    names=['paperID', 'authorID', 'affiliationID', 'paperYear', 'firstPaperYear'])
data1 = data1.drop_duplicates()

data2 = data2[['authorID', 'firstPaperYear']]
data2 = data2.drop_duplicates()

data = data2.merge(data1, on=['authorID'], how='inner')
data = data[['authorID', 'firstPaperYear']]
# 得到了可选的co-author集合

Jieqing_minPaperYear_authorCnt = []
Jieqing_minPaperYear_authorCnt_APPEND = Jieqing_minPaperYear_authorCnt.append

with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        Jieqing_minPaperYear_authorCnt_APPEND((int(line[0]), int(line[1])))
ans_authorID = []
ans_authorID_APPEND = ans_authorID.append
for (minYear, authorCnt) in Jieqing_minPaperYear_authorCnt:
    minYear_group = data[data['firstPaperYear'] == minYear]
    LEN = minYear_group.shape[0]
    if LEN < authorCnt:
        print(minYear, "lack", LEN-authorCnt)
    cnt = 0
    for i in range(0, LEN):
        authorID_i = minYear_group.iloc[i]['authorID']
        ans_authorID_APPEND(authorID_i)
        cnt += 1
        if cnt >= authorCnt:
            break

print(len(ans_authorID))
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\ans_compare_coAuthorID.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    for authorID in ans_authorID:
        f.write(str(authorID)+'\n')