# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组，已经给各个coAuthor假定好了一个assumeAwardYear，后面是根据各个假定好的awardYear去计算四个参数jif、aveCitation、hIndex、paperCnt

已经算好每个coAuthor的paperCnt

算jif
"""
import pandas as pd
from collections import defaultdict


def getAveJIFThisYear(journalID_paperYear_DF, journalID_paperYear_JIF):
    RLEN = journalID_paperYear_DF.shape[0]
    if RLEN == 0:
        return 0
    JIF_sum = 0
    for i in range(0, RLEN):
        journalID = str(journalID_paperYear_DF.iloc[i]['journalID'])
        year = int(journalID_paperYear_DF.iloc[i]['coAuthorPaperYear'])
        JIF_sum += journalID_paperYear_JIF[(journalID, year)]
    return JIF_sum / RLEN


def getJournalJIF( path_jif):
    journalJIF = defaultdict(lambda: 0)
    path = path_jif
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            journalID = str(line[0])
            i = 1
            for year in range(1989, 2018):
                journalJIF[(journalID, year)] = float(line[i])
                i += 1
    return journalJIF


path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
        r"journalID_minYear_maxYear_assumeAwardYear.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\JIF\(all)journalID_JIF_perYear_from1989to2017.txt"
path_out_root = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\co-authorData\\co_author(affID_sortedName)\\4\\"

data = pd.read_csv(path0, sep='\t')
print(data.columns)
data = data[data['journalID'] != '#']
journalID_paperYear_JIF = getJournalJIF(path1)
path_out = path_out_root + "(coAuthor)fxID_jif11Years.txt"
outer = open(path_out, 'w', encoding='utf-8')
data = data.groupby(['fxID', 'assumeAwardYear'])
for fxID_assumeAwardYear, group in data:
    fxID_i = fxID_assumeAwardYear[0]
    assumeAwardYear_i = fxID_assumeAwardYear[1]
    journalID_paperYear1 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -5][['journalID', 'coAuthorPaperYear']]
    jif1 = getAveJIFThisYear(journalID_paperYear1, journalID_paperYear_JIF)
    journalID_paperYear2 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -4][['journalID', 'coAuthorPaperYear']]
    jif2 = getAveJIFThisYear(journalID_paperYear2, journalID_paperYear_JIF)
    journalID_paperYear3 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -3][['journalID', 'coAuthorPaperYear']]
    jif3 = getAveJIFThisYear(journalID_paperYear3, journalID_paperYear_JIF)
    journalID_paperYear4 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -2][['journalID', 'coAuthorPaperYear']]
    jif4 = getAveJIFThisYear(journalID_paperYear4, journalID_paperYear_JIF)
    journalID_paperYear5 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == -1][['journalID', 'coAuthorPaperYear']]
    jif5 = getAveJIFThisYear(journalID_paperYear5, journalID_paperYear_JIF)
    journalID_paperYear6 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 0][['journalID', 'coAuthorPaperYear']]
    jif6 = getAveJIFThisYear(journalID_paperYear6, journalID_paperYear_JIF)
    journalID_paperYear7 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 1][['journalID', 'coAuthorPaperYear']]
    jif7 = getAveJIFThisYear(journalID_paperYear7, journalID_paperYear_JIF)
    journalID_paperYear8 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 2][['journalID', 'coAuthorPaperYear']]
    jif8 = getAveJIFThisYear(journalID_paperYear8, journalID_paperYear_JIF)
    journalID_paperYear9 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 3][['journalID', 'coAuthorPaperYear']]
    jif9 = getAveJIFThisYear(journalID_paperYear9, journalID_paperYear_JIF)
    journalID_paperYear10 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 4][['journalID', 'coAuthorPaperYear']]
    jif10 = getAveJIFThisYear(journalID_paperYear10, journalID_paperYear_JIF)
    journalID_paperYear11 = group[group['coAuthorPaperYear'] - assumeAwardYear_i == 5][['journalID', 'coAuthorPaperYear']]
    jif11 = getAveJIFThisYear(journalID_paperYear11, journalID_paperYear_JIF)
    xl = [jif1, jif2, jif3, jif4, jif5, jif6, jif7, jif8, jif9, jif10, jif11]
    xl = list(map(str, xl))
    outer.write(str(fxID_i)+'\t'+'\t'.join(xl)+'\n')
    pass
outer.close()
