# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
path1 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
path2 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
        r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_citationCnt.txt"
path3 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
        r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_citationCnt_journalID.txt"
colnames = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
            'chineseName', 'awardYear', 'citationCnt']
data1 = pd.read_csv(path1, sep='\t', header=None, names=['paperID', 'year', 'journalID'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=colnames)

data1 = data1[['paperID', 'journalID']]
data1 = data1.drop_duplicates()

data2 = data2.merge(data1, left_on='paperID', right_on='paperID', how='inner')
data2 = data2[['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
                    'chineseName', 'awardYear', 'citationCnt', 'journalID']]
data2.to_csv(path3, sep='\t', header=None, index=False)
