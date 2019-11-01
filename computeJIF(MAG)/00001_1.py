# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
"""
import pandas as pd
path = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
       r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
       r"awardYear_citationCnt.txt"
path1 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
# 找出杰青所投的期刊
pathOut = r"E:\FengXu\result\JIF\JieqingContribute" \
          r"_paperID_year_JournalID.txt"

data1 = pd.read_csv(path, sep='\t', header=None, usecols=[0])
data1.columns = ['paperID']
data1 = data1.drop_duplicates()

colName = ['paperID', 'year', 'journalID']
data2 = pd.read_csv(path1, sep='\t', header=None, names=colName)

data = data1.merge(data2, on=['paperID'], how='inner')
data = data[['paperID', 'year', 'journalID']]
data.to_csv(pathOut, sep='\t', header=None, index=False)
