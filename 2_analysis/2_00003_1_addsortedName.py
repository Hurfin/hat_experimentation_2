# -*- coding: utf-8 -*-
# !/usr/bin/env python

path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperI" \
       r"D_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperI" \
       r"D_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear.txt"


def getSortedName(normalizedName):
    normalizedName_list = normalizedName.split(' ')
    normalizedName_list = sorted()
    normalizedName = ' '.join(normalizedName_list)
    return normalizedName


fout = open(pathOut, 'w', encoding='utf-8')
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        normalizedName = line[4]
        normalizedName_list = line[4].split(' ')
        normalizedName_list.sort()
        sortedName = ' '.join(normalizedName_list)
        x = line
        x.insert(5, sortedName)
        fout.write('\t'.join(x)+'\n')
fout.close()