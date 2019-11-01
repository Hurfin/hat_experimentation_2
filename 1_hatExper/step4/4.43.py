# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组的前后合作密度（以及前后的合作者数量变化）
"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\coAuthorID_fxID_fieldID_fieldName.txt"
上步得到
"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\dz_fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_
journalID_minYear_maxYear_assumeAwardYear.txt"

得到r"E:\FengXu\result3\dzPaperID_authorID_affID.txt"
"""
import pandas as pd
# path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\dz_fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
#         r"journalID_minYear_maxYear_assumeAwardYear.txt"
path0 = r"E:\FengXu\tmp\dz_" \
        r"fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
path1 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"

fxID_paperIDs_set = set()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fxID_paperIDs_set.add(line[2])
    pass

path_out = r"E:\FengXu\result3\dzPaperID_authorID_affID.txt"
outer = open(path_out, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in fxID_paperIDs_set:
            outer.write(line[0]+'\t'+line[1]+'\t'+line[2]+'\n')
outer.close()
