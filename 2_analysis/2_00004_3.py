# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
前5年到后5年的 每年的论文数，citation总数 ，然后相除
"""
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


def main():
    # path1 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_affiliationID" \
    #         r"_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_citationCnt.txt"
    path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
            r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
            r"awardYear_citationCnt.txt"
    pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
            r"aveCitationCntPerYear(before5ANDafter5).txt"
    data = pd.read_csv(path, sep='\t', header=None)
    data.columns = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName', 'chineseName', 'awardYear', 'citationCnt']
    data = data.groupby(['affiliationID', 'sortedName'])
    fout = open(pathOut, 'w', encoding='utf-8')
    for key, group in data:
        papercnt1 = group[group['paperYear'] - group['awardYear'] == -5].shape[0]
        citationSum1 = group[group['paperYear'] - group['awardYear'] == -5]['citationCnt'].sum()
        y1 = 0 if papercnt1 == 0 else citationSum1/papercnt1
        papercnt2 = group[group['paperYear'] - group['awardYear'] == -4].shape[0]
        citationSum2 = group[group['paperYear'] - group['awardYear'] == -4]['citationCnt'].sum()
        y2 = 0 if papercnt2 == 0 else citationSum2/papercnt2
        papercnt3 = group[group['paperYear'] - group['awardYear'] == -3].shape[0]
        citationSum3 = group[group['paperYear'] - group['awardYear'] == -3]['citationCnt'].sum()
        y3 = 0 if papercnt3 == 0 else citationSum3/papercnt3
        papercnt4 = group[group['paperYear'] - group['awardYear'] == -2].shape[0]
        citationSum4 = group[group['paperYear'] - group['awardYear'] == -2]['citationCnt'].sum()
        y4 = 0 if papercnt4 == 0 else citationSum4/papercnt4
        papercnt5 = group[group['paperYear'] - group['awardYear'] == -1].shape[0]
        citationSum5 = group[group['paperYear'] - group['awardYear'] == -1]['citationCnt'].sum()
        y5 = 0 if papercnt5 == 0 else citationSum5/papercnt5
        papercnt6 = group[group['paperYear'] - group['awardYear'] == 0].shape[0]
        citationSum6 = group[group['paperYear'] - group['awardYear'] == 0]['citationCnt'].sum()
        y6 = 0 if papercnt6 == 0 else citationSum6/papercnt6
        papercnt7 = group[group['paperYear'] - group['awardYear'] == 1].shape[0]
        citationSum7 = group[group['paperYear'] - group['awardYear'] == 1]['citationCnt'].sum()
        y7 = 0 if papercnt7 == 0 else citationSum7/papercnt7
        papercnt8 = group[group['paperYear'] - group['awardYear'] == 2].shape[0]
        citationSum8 = group[group['paperYear'] - group['awardYear'] == 2]['citationCnt'].sum()
        y8 = 0 if papercnt8 == 0 else citationSum8/papercnt8
        papercnt9 = group[group['paperYear'] - group['awardYear'] == 3].shape[0]
        citationSum9 = group[group['paperYear'] - group['awardYear'] == 3]['citationCnt'].sum()
        y9 = 0 if papercnt9 == 0 else citationSum9/papercnt9
        papercnt10 = group[group['paperYear'] - group['awardYear'] == 4].shape[0]
        citationSum10 = group[group['paperYear'] - group['awardYear'] == 4]['citationCnt'].sum()
        y10 = 0 if papercnt10 == 0 else citationSum10/papercnt10
        papercnt11 = group[group['paperYear'] - group['awardYear'] == 5].shape[0]
        citationSum11 = group[group['paperYear'] - group['awardYear'] == 5]['citationCnt'].sum()
        y11 = 0 if papercnt11 == 0 else citationSum11/papercnt11

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
    pass


