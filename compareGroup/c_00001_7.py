# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

# path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
#         r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_" \
#         r"chineseName_awardYear_citationCnt.txt"
# pathOut1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\Jieqing_firstPaperYear.txt"
# pathOut2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\firstYear_authorCnt.txt"
# names = ['affiliationID', 'paperYear', 'sortedName']
#
# data = pd.read_csv(path1, sep='\t', header=None, names=names, usecols=[2, 5, 3])
#
# data = data.groupby(['affiliationID', 'sortedName'])['paperYear'].min()
# data = data.reset_index()
# data.columns = ['affiliationID', 'sortedName', 'minPaperYear']
#
# data.to_csv(pathOut1, sep='\t', header=None, index=False)
#
# data = data.groupby('minPaperYear')
# DICT = {
#     'minPaperYear': [],
#     'paperCnt': []
# }
# for minPaperYear, group in data:
#     paperCnt = group.shape[0]
#     DICT['minPaperYear'].append(minPaperYear)
#     DICT['paperCnt'].append(paperCnt)
#
# data = pd.DataFrame(DICT)
# print(data.head(2))
#
# data.to_csv(pathOut2, sep='\t', header=None, index=False)

path = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge" \
       r"(academicAge5_25).txt"

data = pd.read_csv(path, sep='\t', header=None, usecols=[0, 1, 2], names=['affiliationID', 'sortedName', 'minYear'])

data = data.groupby('minYear')
D = {
    'minYear': [],
    'authorCnt': []
}
for minYear, group in data:
    authorCnt = group.shape[0]
    D['minYear'].append(minYear)
    D['authorCnt'].append(authorCnt)
data = pd.DataFrame(D)
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\Jieqing_minPaperYear_authorCnt.txt"
data = data[['minYear', 'authorCnt']]
data.to_csv(pathOut, sep='\t', header=None, index=False)
