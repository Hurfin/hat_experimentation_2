# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算学者的每年的平均论文JIF
"""
import numpy as np
import pandas as pd
from collections import defaultdict


def leastSqrt(Xi, Yi):
    sum_xi_yi = 0
    sum_xi = 0
    sum_yi = 0
    sum_xi_sq = 0
    n = len(Xi)
    for i in range(0, len(Xi)):
        sum_xi_yi += Xi[i] * Yi[i]
        sum_xi += Xi[i]
        sum_yi += Yi[i]
        sum_xi_sq += Xi[i] * Xi[i]
    k = (n * sum_xi_yi - sum_xi * sum_yi) / (n * sum_xi_sq - sum_xi * sum_xi)
    b = (sum_yi - k * sum_xi) / n
    return k, b


def getJournalJIF():
    journalJIF = defaultdict(lambda: 0)
    path = r"E:\pythonCode\RJ_experimentation_1\Data\result\JIFfrom1989to2017_MAG_JieqingContributeJournal\journalID_JIF_perYear_from1989to2017.txt"
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('\t')
            journalID = str(int(float(line[0])))
            i = 1
            for year in range(1989, 2018):
                journalJIF[(journalID, year)] = float(line[i])
                i += 1
        pass
    return journalJIF
    pass


def getAveJIFThisYear(journalID_paperYear_DF, journalID_paperYear_JIF):
    RLEN = journalID_paperYear_DF.shape[0]
    if RLEN == 0:
        return 0
    JIF_sum = 0
    for i in range(0, RLEN):
        journalID = str(int(float(journalID_paperYear_DF.iloc[i]['DZ_journalID'])))
        year = int(journalID_paperYear_DF.iloc[i]['DZ_paperYear'])
        JIF_sum += journalID_paperYear_JIF[(journalID, year)]
    return JIF_sum / RLEN


path1 = r"E:\pythonCode\RJ_experimentation_1\Data\TMP\DZ_paperID_journalID.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(DZ)" \
        r"DZ_paperID_DZ_authorID_DZ_affiliationID_DZ_paperYear_DZ_firstPaperYear_JQ_affiliationID_" \
        r"JQ_sortedName_DZ_assumeAwardYear_DZ_citationCnt.txt"

names = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
         'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName', 'DZ_assumeAwardYear', 'DZ_citationCnt']
data1 = pd.read_csv(path1, sep='\t', header=None, names=['DZ_paperID', 'DZ_journalID'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=names)

data = pd.merge(data1, data2, on=['DZ_paperID'], how='inner')
selectCols = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
              'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName',
              'DZ_assumeAwardYear', 'DZ_citationCnt', 'DZ_journalID']
data = data[selectCols]
del data1, data2

data = data.groupby(['DZ_authorID', 'DZ_assumeAwardYear'])
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear" \
          r"_k1_b1_k2_b2_aveJIFPerYear(Before5ANDafter5).txt"
fout = open(pathOut, 'w', encoding='utf-8')
journalID_paperYear_JIF = getJournalJIF()

for DZ_authorID_awardYear, group in data:
    DZ_authorID = DZ_authorID_awardYear[0]
    DZ_awardYear = DZ_authorID_awardYear[1]

    journalID_paperYear1 = group[group['DZ_paperYear'] - DZ_awardYear == -5][['DZ_journalID', 'DZ_paperYear']]
    y1 = getAveJIFThisYear(journalID_paperYear1, journalID_paperYear_JIF)
    journalID_paperYear2 = group[group['DZ_paperYear'] - DZ_awardYear == -4][['DZ_journalID', 'DZ_paperYear']]
    y2 = getAveJIFThisYear(journalID_paperYear2, journalID_paperYear_JIF)
    journalID_paperYear3 = group[group['DZ_paperYear'] - DZ_awardYear == -3][['DZ_journalID', 'DZ_paperYear']]
    y3 = getAveJIFThisYear(journalID_paperYear3, journalID_paperYear_JIF)
    journalID_paperYear4 = group[group['DZ_paperYear'] - DZ_awardYear == -2][['DZ_journalID', 'DZ_paperYear']]
    y4 = getAveJIFThisYear(journalID_paperYear4, journalID_paperYear_JIF)
    journalID_paperYear5 = group[group['DZ_paperYear'] - DZ_awardYear == -1][['DZ_journalID', 'DZ_paperYear']]
    y5 = getAveJIFThisYear(journalID_paperYear5, journalID_paperYear_JIF)
    journalID_paperYear6 = group[group['DZ_paperYear'] - DZ_awardYear == 0][['DZ_journalID', 'DZ_paperYear']]
    y6 = getAveJIFThisYear(journalID_paperYear6, journalID_paperYear_JIF)
    journalID_paperYear7 = group[group['DZ_paperYear'] - DZ_awardYear == 1][['DZ_journalID', 'DZ_paperYear']]
    y7 = getAveJIFThisYear(journalID_paperYear7, journalID_paperYear_JIF)
    journalID_paperYear8 = group[group['DZ_paperYear'] - DZ_awardYear == 2][['DZ_journalID', 'DZ_paperYear']]
    y8 = getAveJIFThisYear(journalID_paperYear8, journalID_paperYear_JIF)
    journalID_paperYear9 = group[group['DZ_paperYear'] - DZ_awardYear == 3][['DZ_journalID', 'DZ_paperYear']]
    y9 = getAveJIFThisYear(journalID_paperYear9, journalID_paperYear_JIF)
    journalID_paperYear10 = group[group['DZ_paperYear'] - DZ_awardYear == 4][['DZ_journalID', 'DZ_paperYear']]
    y10 = getAveJIFThisYear(journalID_paperYear10, journalID_paperYear_JIF)
    journalID_paperYear11 = group[group['DZ_paperYear'] - DZ_awardYear == 5][['DZ_journalID', 'DZ_paperYear']]
    y11 = getAveJIFThisYear(journalID_paperYear11, journalID_paperYear_JIF)

    xi1 = [-5, -4, -3, -2, -1]
    yi1 = [y1, y2, y3, y4, y5]
    k1, b1 = leastSqrt(xi1, yi1)

    xi2 = [1, 2, 3, 4, 5]
    yi2 = [y7, y8, y9, y10, y11]
    k2, b2 = leastSqrt(xi2, yi2)

    Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11]
    Y = list(map(str, Y))
    fout.write(str(DZ_authorID) + '\t' + str(DZ_awardYear) + '\t' + str(k1) + '\t' + str(b1) + '\t' + str(k2) + '\t' +
               str(b2) + '\t' + '\t'.join(Y) + '\n')
fout.close()
