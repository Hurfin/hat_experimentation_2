# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import pandas as pd
from collections import Counter


def getAuthorField(fatherFieldID_list):
    counter = Counter(fatherFieldID_list)
    return counter.most_common(1)[0][0]


path = r"E:\pythonCode\RJ_experimentation_1\Data\field\ans_paperID_fatherFieldID.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
        r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
        r"awardYear_citationCnt.txt"
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\field\affiliationID_sortedName_fatherFieldID.txt"
names1 = ['paperID', 'affiliationID', 'sortedName']
data1 = pd.read_csv(path1, sep='\t', header=None, names=names1, usecols=[0, 2, 5])

names2 = ['paperID', 'fatherFieldID']
data2 = pd.read_csv(path, sep='\t', header=None, names=names2)

data = pd.merge(data1, data2, on=['paperID'], how='inner')
del data1, data2

data = data[['paperID', 'affiliationID', 'sortedName', 'fatherFieldID']]
fout = open(pathOut, 'w', encoding='utf-8')
data = data.groupby(['affiliationID', 'sortedName'])
for affID_sortedName, group in data:
    authorFieldID = getAuthorField(list(group['fatherFieldID']))
    fout.write(str(affID_sortedName[0])+'\t'+str(affID_sortedName[1])+'\t'+str(authorFieldID)+'\n')
fout.close()
