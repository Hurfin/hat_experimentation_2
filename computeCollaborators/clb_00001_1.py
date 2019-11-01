# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_paperYear_firstPaperYear(Co).txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_paperYear(JQ_Co).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_paperYear(Co).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\Jieqing_paperIDs.txt"
path4 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\Jieqing_authorID.txt"

path5 = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge(academicAge5_25).txt"
path6 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
        r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
        r"awardYear_citationCnt.txt"

names1 = ['affiliationID', 'sortedName']
data1 = pd.read_csv(path5, sep='\t', header=None, names=names1, usecols=[0, 1])
names2 = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear', 'citationCnt']
data2 = pd.read_csv(path6, sep='\t', header=None, names=names2)

data3 = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'authorID', 'affiliationID', 'paperYear'])
# 首先筛选出这1210个杰青数据
# 然后把他们按key，groupby，得到一个杰青一个分组
# 对groupby后的一个分组，对于他的每个paper id，查询在path2中有多少行，那这个论文就有多少个co-author
# 把co-author数目统计出来（用set保存，使用len），并保留co-author id
# 前五年完毕后，相同办法算后五年，从中去掉前五年的co-author，查数量

data = pd.merge(data1, data2, on=['affiliationID', 'sortedName'], how='inner')
del data1, data2
data = data[['paperID', 'authorID', 'affiliationID', 'paperYear', 'sortedName', 'awardYear', 'citationCnt']]

data = data.groupby(['affiliationID', 'sortedName'])

fout = open(
    r"E:\pythonCode\RJ_experimentation_1\Data\result\experment2_result\1result\collaboratorsBeforeAndAfter5year.txt",
    'w', encoding='utf-8')

for affID_sortedName, group in data:
    # 对于一个学者，先选出他前五年和后五年的论文
    # before5 = group[(-5 <= (group['paperYear'] - group['awardYear']) <= -1)][['paperID']]
    # after5 = group[(1 <= (group['paperYear'] - group['awardYear']) <= 5)][['paperID']]

    before5 = group[(-5 <= (group['paperYear'] - group['awardYear']))&((group['paperYear'] - group['awardYear']) <= -1)][['paperID']]
    after5 = group[(1 <= (group['paperYear'] - group['awardYear']))&((group['paperYear'] - group['awardYear']) <= 5)][['paperID']]


    before5 = before5.drop_duplicates()
    after5 = after5.drop_duplicates()

    before5_coAuthor = pd.merge(data3, before5, on=['paperID'])['authorID']
    after5_coAuthor = pd.merge(data3, after5, on=['paperID'])['authorID']


    before5_coAuthor_set = set(list(before5_coAuthor))
    after5_coAuthor_set = set(list(after5_coAuthor))

    collaborators_before = len(before5_coAuthor_set)
    collaborators_after = len((after5_coAuthor_set - before5_coAuthor_set))
    fout.write(str(affID_sortedName[0])+'\t'+str(affID_sortedName[1])+'\t'+str(collaborators_before)+'\t'+str(collaborators_after)+'\n')
fout.close()