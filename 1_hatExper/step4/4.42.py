# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组的前后合作密度（以及前后的合作者数量变化）
"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\coAuthorID_fxID_fieldID_fieldName.txt"
得到
"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\dz_fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_
journalID_minYear_maxYear_assumeAwardYear.txt"
"""
import pandas as pd
# path0 = r"E:\FengXu\tmp\coAuthorID_fxID_fieldID_fieldName.txt"
path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\coAuthorID_fxID_fieldID_fieldName.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
        r"journalID_minYear_maxYear_assumeAwardYear.txt"

coAuthor_fxID = set()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        coAuthor_fxID.add(line[1])
    pass
print(len(coAuthor_fxID))
flag_fxID = set()
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\dz_fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
        r"journalID_minYear_maxYear_assumeAwardYear.txt"
outer = open(path2, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in coAuthor_fxID:
            outer.write('\t'.join(line)+'\n')
            flag_fxID.add(line[0])
            pass
    pass
outer.close()
print(len(coAuthor_fxID - flag_fxID))
print(len(flag_fxID - coAuthor_fxID))
