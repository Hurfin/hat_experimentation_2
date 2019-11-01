# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
先把几个领域的杰青的数据合并起来，再把field id和field name加上去
"""
import pandas as pd
import os
import csv

path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\field\affID_sortedName_fieldID_fieldName.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_" \
        r"JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_" \
        r"displayName_chineseName_awardYear_citationCnt.txt"
names1 = ['affiliationID', 'sortedName', 'fieldID', 'fieldName']
names2 = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
          'chineseName', 'awardYear', 'citationCnt']
data1 = pd.read_csv(path0, sep='\t', header=None, names=names1)
data2 = pd.read_csv(path1, sep='\t', header=None, names=names2)

data = pd.merge(data1, data2, on=['affiliationID', 'sortedName'], how='inner')
del data1, data2

sortBy = ['affiliationID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID',
          'paperYear', 'awardYear', 'citationCnt']
data = data[sortBy]

pathOut = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ" + "\\JQ_" + '_'.join(sortBy) + ".txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)
