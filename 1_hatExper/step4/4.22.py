# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已有
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_minYear_maxYear.txt"

找co-author paper id的journal id，然后看看有哪些journal id之前没有被计算，计算出来这些期刊在各个年份的JIF值
首先得找到coAuthorPaperID对应的是不是journal，是journal的话，journal id是什么

"""
import pandas as pd
import csv

path1 = r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_minYear_maxYear.txt"
path2 = r"D:\Dataset\NEW_MAG\Papers.txt"

coAuthorPaperID_set = set()
flag = True
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        if flag is True:
            flag = False
            continue
        line = line.strip('\n').split('\t')
        coAuthorPaperID_set.add(line[2])
    pass

path_out1 = r"E:\FengXu\result1\coAuthorPaperID_journalID.txt"
outer1 = open(path_out1, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[3] == 'Journal' and line[10] is not None and line[10] != '':
            if line[0] in coAuthorPaperID_set:
                outer1.write(line[0]+'\t'+line[10]+'\n')
            pass
    pass
outer1.close()
