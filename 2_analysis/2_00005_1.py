# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
h-index
"""
import os
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
    pass


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


def main():
    path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
            r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
            r"awardYear_citationCnt.txt"
    path2 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
            r"h-IndexPerYear(before5ANDafter5).txt"
    data = pd.read_csv(path1, sep='\t', header=None)
    data.columns = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
                    'chineseName', 'awardYear', 'citationCnt']
    data = data.groupby(['affiliationID', 'sortedName'])
    fout = open(path2, 'w', encoding='utf-8')
    for key, group in data:
        df1 = list(group[group['paperYear']-group['awardYear'] <= -5]['citationCnt'])
        y1 = h_index(df1)
        df2 = list(group[group['paperYear'] - group['awardYear'] <= -4]['citationCnt'])
        y2 = h_index(df2)
        df3 = list(group[group['paperYear'] - group['awardYear'] <= -3]['citationCnt'])
        y3 = h_index(df3)
        df4 = list(group[group['paperYear'] - group['awardYear'] <= -2]['citationCnt'])
        y4 = h_index(df4)
        df5 = list(group[group['paperYear'] - group['awardYear'] <= -1]['citationCnt'])
        y5 = h_index(df5)
        df6 = list(group[group['paperYear'] - group['awardYear'] <= 0]['citationCnt'])
        y6 = h_index(df6)
        df7 = list(group[group['paperYear'] - group['awardYear'] <= 1]['citationCnt'])
        y7 = h_index(df7)
        df8 = list(group[group['paperYear'] - group['awardYear'] <= 2]['citationCnt'])
        y8 = h_index(df8)
        df9 = list(group[group['paperYear'] - group['awardYear'] <= 3]['citationCnt'])
        y9 = h_index(df9)
        df10 = list(group[group['paperYear'] - group['awardYear'] <= 4]['citationCnt'])
        y10 = h_index(df10)
        df11 = list(group[group['paperYear'] - group['awardYear'] <= 5]['citationCnt'])
        y11 = h_index(df11)

        xi1 = [-5, -4, -3, -2, -1]
        yi1 = [y1, y2, y3, y4, y5]
        k1, b1 = leastSqrt(xi1, yi1)

        xi2 = [1, 2, 3, 4, 5]
        yi2 = [y7, y8, y9, y10, y11]
        k2, b2 = leastSqrt(xi2, yi2)

        Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11]
        Y = list(map(str, Y))

        fout.write(str(key[0]) + '\t' + str(key[1]) + '\t' + str(k1) + '\t' + str(b1) + '\t' + str(k2) + '\t' + str(
            b2) + '\t' + '\t'.join(Y) + '\n')
        pass
    fout.close()
    pass


if __name__ == '__main__':
    main()