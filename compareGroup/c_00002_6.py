# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算对照组每年的h-index
"""
import numpy as np
import pandas as pd

def h_index(citations):
    citations.sort(reverse=True)
    citations.append(0)
    ans = 0
    for i in range(0, len(citations)):
        if citations[i] < i + 1:
            ans = i
            break
    return ans

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
       r"JQ_sortedName_DZ_assumeAwardYear_DZ_citationCnt.txt"
names = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
         'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName', 'DZ_assumeAwardYear', 'DZ_citationCnt']
data = pd.read_csv(path, sep='\t', header=None, names=names)

data = data.groupby(['DZ_authorID', 'DZ_assumeAwardYear'])
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear" \
          r"_k1_b1_k2_b2_h-indexPerYear(Before5ANDafter5).txt"
fout = open(pathOut, 'w', encoding='utf-8')

for DZ_authorID_awardYear, group in data:
    DZ_authorID = DZ_authorID_awardYear[0]
    DZ_awardYear = DZ_authorID_awardYear[1]

    df1 = list(group[group['DZ_paperYear'] - DZ_awardYear <= -5]['DZ_citationCnt'])
    y1 = h_index(df1)
    df2 = list(group[group['DZ_paperYear'] - DZ_awardYear <= -4]['DZ_citationCnt'])
    y2 = h_index(df2)
    df3 = list(group[group['DZ_paperYear'] - DZ_awardYear <= -3]['DZ_citationCnt'])
    y3 = h_index(df3)
    df4 = list(group[group['DZ_paperYear'] - DZ_awardYear <= -2]['DZ_citationCnt'])
    y4 = h_index(df4)
    df5 = list(group[group['DZ_paperYear'] - DZ_awardYear <= -1]['DZ_citationCnt'])
    y5 = h_index(df5)
    df6 = list(group[group['DZ_paperYear'] - DZ_awardYear <= 0]['DZ_citationCnt'])
    y6 = h_index(df6)
    df7 = list(group[group['DZ_paperYear'] - DZ_awardYear <= 1]['DZ_citationCnt'])
    y7 = h_index(df7)
    df8 = list(group[group['DZ_paperYear'] - DZ_awardYear <= 2]['DZ_citationCnt'])
    y8 = h_index(df8)
    df9 = list(group[group['DZ_paperYear'] - DZ_awardYear <= 3]['DZ_citationCnt'])
    y9 = h_index(df9)
    df10 = list(group[group['DZ_paperYear'] - DZ_awardYear <= 4]['DZ_citationCnt'])
    y10 = h_index(df10)
    df11 = list(group[group['DZ_paperYear'] - DZ_awardYear <= 5]['DZ_citationCnt'])
    y11 = h_index(df11)

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