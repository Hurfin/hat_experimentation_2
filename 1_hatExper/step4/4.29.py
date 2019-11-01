# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
r"journalID_minYear_maxYear_assumeAwardYear.txt"

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\JIF\(all)journalID_JIF_perYear_from1989to2017.txt"
找对照组，已经给各个coAuthor假定好了一个assumeAwardYear，后面是根据各个假定好的awardYear去计算四个参数jif、aveCitation、hIndex、paperCnt

先算每个coAuthor的paperCnt
"""
import pandas as pd
import csv

path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
        r"journalID_minYear_maxYear_assumeAwardYear.txt"
path_out_root = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\co-authorData\\co_author(affID_sortedName)\\4\\"

# fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear	journalID	minYear	maxYear	assumeAwardYear
data1 = pd.read_csv(path0, sep='\t')
# data2 = pd.read_csv()
# print(list(set(list(data1['assumeAwardYear']))))

# print(data1[['fxID', 'assumeAwardYear']].drop_duplicates().shape[0])
# print(data1[['fxID', 'assumeAwardYear']].shape[0])
# print(data1[['fxID']].drop_duplicates().shape[0])
#
# print(data1[['fxID', 'minYear']].drop_duplicates().shape[0])
# print(data1[['fxID']].drop_duplicates().shape[0])

path_out = path_out_root + "(coAuthor)fxID_PaperCnt11Years.txt"
outer = open(path_out, 'w', encoding='utf-8')
data1 = data1.groupby(['fxID', 'assumeAwardYear'])
for fxID_assumeAwardYear, group in data1:
    fxID_i = fxID_assumeAwardYear[0]
    assumeAwardYear_i = fxID_assumeAwardYear[1]
    paperCnt1 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -5].shape[0]
    paperCnt2 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -4].shape[0]
    paperCnt3 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -3].shape[0]
    paperCnt4 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -2].shape[0]
    paperCnt5 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -1].shape[0]
    paperCnt6 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 0].shape[0]
    paperCnt7 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 1].shape[0]
    paperCnt8 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 2].shape[0]
    paperCnt9 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 3].shape[0]
    paperCnt10 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 4].shape[0]
    paperCnt11 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 5].shape[0]

    ans_ = [paperCnt1, paperCnt2, paperCnt3, paperCnt4, paperCnt5, paperCnt6,
            paperCnt7, paperCnt8, paperCnt9, paperCnt10, paperCnt11]
    ans_ = list(map(str, ans_))
    outer.write(str(fxID_i)+'\t'+'\t'.join(ans_)+'\n')
    pass
outer.close()