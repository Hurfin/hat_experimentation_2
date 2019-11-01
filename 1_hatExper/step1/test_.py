# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path = r"C:\Users\12433\Desktop\need_data\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_" \
       r"affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_citationCnt.txt"
data = pd.read_csv(path, sep='\t', header=None, usecols=[5], names=['sortedName'])

names = list(data['sortedName'])
chineseName = dict()
for name in names:
    flag = 0
    for ch in name:
        if not ('a' <= ch <= 'z' or ch == ' '):
            flag = 1
            break
    if flag == 1:  # 中文名
        if name not in chineseName.keys():
            chineseName[name] = 1
        chineseName[name] += 1

print(len(chineseName))
for nm, cnt in chineseName.items():
    print(nm, cnt)