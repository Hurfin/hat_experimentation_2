# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
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


path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperI" \
       r"D_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear.txt"
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
          r"paperCntPerYear(Before5ANDafter5).txt"
data = pd.read_csv(path, sep='\t', header=None)
data.columns = \
    ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear']

data = data.groupby(['affiliationID', 'sortedName'])

fout = open(pathOut, 'w', encoding='utf-8')
# print(data.keys)
# 计算每个学者的获奖前n年和后n年时发的论文数。然后用最小二乘法计算m1、m2
# xi = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for key, group in data:
    # print(key[0], key[1])
    # yi = []
    # group = group.drop_duplicates()
    y1 = group[group['paperYear']-group['awardYear'] == -5].shape[0]
    y2 = group[group['paperYear'] - group['awardYear'] == -4].shape[0]
    y3 = group[group['paperYear'] - group['awardYear'] == -3].shape[0]
    y4 = group[group['paperYear'] - group['awardYear'] == -2].shape[0]
    y5 = group[group['paperYear'] - group['awardYear'] == -1].shape[0]
    y6 = group[group['paperYear'] - group['awardYear'] == 0].shape[0]
    y7 = group[group['paperYear'] - group['awardYear'] == 1].shape[0]
    y8 = group[group['paperYear'] - group['awardYear'] == 2].shape[0]
    y9 = group[group['paperYear'] - group['awardYear'] == 3].shape[0]
    y10 = group[group['paperYear'] - group['awardYear'] == 4].shape[0]
    y11 = group[group['paperYear'] - group['awardYear'] == 5].shape[0]

    xi1 = [-5, -4, -3, -2, -1]
    yi1 = [y1, y2, y3, y4, y5]
    k1, b1 = leastSqrt(xi1, yi1)
    # print(k1, b1)

    xi2 = [1, 2, 3, 4, 5]
    yi2 = [y7, y8, y9, y10, y11]
    k2, b2 = leastSqrt(xi2, yi2)
    # print(k2, b2)
    # print(key[0], key[1], k1, k2)

    Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11]
    Y = list(map(str, Y))
    fout.write(str(key[0])+'\t'+str(key[1])+'\t'+str(k1)+'\t'+str(b1)+'\t'+str(k2)+'\t'+str(b2)+'\t'+'\t'.join(Y)+'\n')
fout.close()
