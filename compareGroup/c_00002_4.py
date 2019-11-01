# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算对照组的 paper count
"""
import pandas as pd


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


path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(DZ)" \
       r"DZ_paperID_DZ_authorID_DZ_affiliationID_DZ_paperYear_DZ_firstPaperYear_JQ_affiliationID_" \
       r"JQ_sortedName_DZ_assumeAwardYear.txt"
names = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
         'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName', 'DZ_assumeAwardYear']
data = pd.read_csv(path, sep='\t', header=None, names=names)

data = data.groupby(['DZ_authorID', 'DZ_assumeAwardYear'])
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear" \
          r"_k1_b1_k2_b2_paperCntPerYear(Before5ANDafter5).txt"
fout = open(pathOut, 'w', encoding='utf-8')
for DZ_authorID_awardYear, group in data:
    DZ_authorID = DZ_authorID_awardYear[0]
    DZ_awardYear = DZ_authorID_awardYear[1]

    y1 = group[group['DZ_paperYear'] == DZ_awardYear - 5].shape[0]
    y2 = group[group['DZ_paperYear'] == DZ_awardYear - 4].shape[0]
    y3 = group[group['DZ_paperYear'] == DZ_awardYear - 3].shape[0]
    y4 = group[group['DZ_paperYear'] == DZ_awardYear - 2].shape[0]
    y5 = group[group['DZ_paperYear'] == DZ_awardYear - 1].shape[0]
    y6 = group[group['DZ_paperYear'] == DZ_awardYear].shape[0]
    y7 = group[group['DZ_paperYear'] == DZ_awardYear + 1].shape[0]
    y8 = group[group['DZ_paperYear'] == DZ_awardYear + 2].shape[0]
    y9 = group[group['DZ_paperYear'] == DZ_awardYear + 3].shape[0]
    y10 = group[group['DZ_paperYear'] == DZ_awardYear + 4].shape[0]
    y11 = group[group['DZ_paperYear'] == DZ_awardYear + 5].shape[0]

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
