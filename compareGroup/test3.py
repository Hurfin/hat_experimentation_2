# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as np
import pandas as pd

# path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
#         r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
#         r"awardYear_citationCnt.txt"
# names1 = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear', 'citationCnt']
# data1 = pd.read_csv(path1, sep='\t', header=None, names=names1)
# awardYearList = np.array(data1['awardYear'])
# print(min(awardYearList), awardYearList.max())

# path = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge(academicAge5_25).txt"
# names = ['affiliationID', 'sortedName', 'minYear', 'awardYear', 'academicAge']
# data = pd.read_csv(path, sep='\t', header=None,names=names)
# data = data[['academicAge']]
# data = data.drop_duplicates()
# ages = np.array(data['academicAge'])
# ages.sort()
# print(ages)

# path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
#        r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_" \
#        r"chineseName_awardYear_citationCnt.txt"
#
# data = pd.read_csv(path, sep='\t', header=None, names=['affiliationID', 'sortedName'], usecols=[2, 5])
# data = data.drop_duplicates()
# print(data.shape[0])

import pickle as pk
f = open(r"C:\Users\12433\Desktop\award_ex\award_ex\data\期刊影响因子.pkl", 'rb')
info = pk.load(f)
print(len(info))
