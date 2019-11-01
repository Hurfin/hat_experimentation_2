# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""

"""
import pandas as pd
path1 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_affiliationID" \
        r"_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear.txt"
path2 = r'E:\FengXu\result\paperID_citationCnt(jieqing).txt'

pathOut1 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_affiliationID" \
           r"_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_citationCnt.txt"
data1 = pd.read_csv(path1, sep='\t', header=None)
data1.columns = \
    ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear']


data2 = pd.read_csv(path2, sep='\t', header=None)
data2.columns = ['paperID1', 'citationCnt']

data1 = data1.merge(data2, left_on=['paperID'], right_on=['paperID1'], how='left')
data1 = data1[['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear', 'citationCnt']]

data1 = data1.fillna(0)
data1 = data1.drop_duplicates()
data1 = data1.astype({'citationCnt': int})

data1.to_csv(pathOut1, sep='\t', header=None, index=False)
