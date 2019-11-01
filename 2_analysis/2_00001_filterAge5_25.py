# -*- coding: utf-8 -*-
# !/usr/bin/env python

path = r"C:\Users\12433\Desktop\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge.txt"
outPath = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge(academicAge5_25).txt"

affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge.append(line)

outPath1 = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge(age_lower5_upper25).txt"
fout1 = open(outPath1, 'w', encoding='utf-8')
fout = open(outPath, 'w', encoding='utf-8')
for i in range(0, len(affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge)):
    if int(affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i][4]) < 5 or int(affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i][4]) > 25:
        print(affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i][0], affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i][1],
              affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i][4], sep='\t')
        fout1.write('\t'.join(affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i])+'\n')
    else:
        x = affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge[i]
        fout.write('\t'.join(x)+'\n')
fout.close()
fout1.close()
