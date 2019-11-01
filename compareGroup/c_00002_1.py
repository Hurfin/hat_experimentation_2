# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge"\
       r"(academicAge5_25).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_" \
        r"paperYear_firstPaperYear(Co).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthor_age5_25_Aff_CN_paperNum5more.txt"
# 杰青、first year
data1 = pd.read_csv(path1, sep='\t', header=None, names=['affiliationID', 'sortedName', 'minYear'], usecols=[0, 1, 2])
# 候选者的author id，first year
data2 = pd.read_csv(path2, sep='\t', header=None, names=['authorID', 'firstPaperYear'], usecols=[1, 4])
data2 = data2.drop_duplicates()
data_tmp = pd.read_csv(path3, sep='\t', header=None, names=['authorID'])
data2 = data2.merge(data_tmp, on=['authorID'], how='inner')
data2 = data2[['authorID', 'firstPaperYear']]
del data_tmp

# 杰青按minYear聚合
data1 = data1.groupby('minYear')
# data2 = data2.groupby('firstPaperYear')
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\ans_JQ_map_coAuthor.txt"
fout = open(pathOut, 'w', encoding='utf-8')
for minYear, group1 in data1:  # 杰青
    group1_len = group1.shape[0]
    data2_group = data2[data2['firstPaperYear'] == minYear]  # 候选者中，第一篇论文年份等于该年的
    for i in range(0, group1_len):  # 对于杰青的每个人
        compareAuID = data2_group.iloc[i]['authorID']
        JQ_sortedName = group1.iloc[i]['sortedName']
        JQ_affiliationID = group1.iloc[i]['affiliationID']
        fout.write(str(JQ_affiliationID)+'\t'+str(JQ_sortedName)+'\t'+str(compareAuID)+'\n')
        pass
    pass
fout.close()
