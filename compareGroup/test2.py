# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
       r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
       r"awardYear_citationCnt.txt"
names1 = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear', 'citationCnt']
data = pd.read_csv(path, sep='\t', header=None, names=names1)

np.array(data['awardYear'])
# print(data[['awardYear']].min(), data[['awardYear']].max())