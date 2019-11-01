# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path1 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_affiliationID" \
        r"_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear.txt"
path2 = r"D:\Dataset\NEW_MAG\PaperReferences.txt"


pathOut1 = r'E:\FengXu\result\paperID_referenceID(jieqing).txt'
pathOut2 = r'E:\FengXu\result\paperID_citationCnt(jieqing).txt'

data1 = pd.read_csv(path1, sep='\t', header=None, usecols=[0])
data1.columns = ['paperID_jieqing']
data1 = data1.drop_duplicates()

data2 = pd.read_csv(path2, sep='\t', header=None)
data2.columns = ['paperID', 'referenceID']
data2 = data2.drop_duplicates()

data2 = data2.merge(data1, left_on=['referenceID'], right_on=['paperID_jieqing'], how='inner')
data2 = data2[['paperID', 'referenceID']]
del data1

data2.to_csv(pathOut1, sep='\t', header=None, index=False)

paperID_citationCnt = data2.groupby('referenceID').count()
paperID_citationCnt = paperID_citationCnt.reset_index()
paperID_citationCnt.columns = ['paperID', 'citationCnt']

paperID_citationCnt.to_csv(pathOut2, sep='\t', header=None, index=False)
