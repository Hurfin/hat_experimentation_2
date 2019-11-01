# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算各个学者的JIF
"""
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
        journalID = str(int(float(journalID_paperYear_DF.iloc[i]['journalID'])))
        year = int(journalID_paperYear_DF.iloc[i]['paperYear'])
        JIF_sum += journalID_paperYear_JIF[(journalID, year)]
    return JIF_sum / RLEN
    pass


def main():
    path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
            r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
            r"awardYear_citationCnt_journalID.txt"
    path2 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
            r"aveJIFPerYear(before5ANDafter5).txt"
    data = pd.read_csv(path1, sep='\t', header=None)
    data.columns = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
                    'chineseName', 'awardYear', 'citationCnt', 'journalID']
    data = data[data['awardYear'] <= 2013]
    data = data.groupby(['affiliationID', 'sortedName'])
    journalID_paperYear_JIF = getJournalJIF()
    fout = open(path2, 'w', encoding='utf-8')
    for key, group in data:
        journalID_paperYear1 = group[group['paperYear'] - group['awardYear'] == -5][['journalID', 'paperYear']]
        y1 = getAveJIFThisYear(journalID_paperYear1, journalID_paperYear_JIF)
        journalID_paperYear2 = group[group['paperYear'] - group['awardYear'] == -4][['journalID', 'paperYear']]
        y2 = getAveJIFThisYear(journalID_paperYear2, journalID_paperYear_JIF)
        journalID_paperYear3 = group[group['paperYear'] - group['awardYear'] == -3][['journalID', 'paperYear']]
        y3 = getAveJIFThisYear(journalID_paperYear3, journalID_paperYear_JIF)
        journalID_paperYear4 = group[group['paperYear'] - group['awardYear'] == -2][['journalID', 'paperYear']]
        y4 = getAveJIFThisYear(journalID_paperYear4, journalID_paperYear_JIF)
        journalID_paperYear5 = group[group['paperYear'] - group['awardYear'] == -1][['journalID', 'paperYear']]
        y5 = getAveJIFThisYear(journalID_paperYear5, journalID_paperYear_JIF)
        journalID_paperYear6 = group[group['paperYear'] - group['awardYear'] == 0][['journalID', 'paperYear']]
        y6 = getAveJIFThisYear(journalID_paperYear6, journalID_paperYear_JIF)
        journalID_paperYear7 = group[group['paperYear'] - group['awardYear'] == 1][['journalID', 'paperYear']]
        y7 = getAveJIFThisYear(journalID_paperYear7, journalID_paperYear_JIF)
        journalID_paperYear8 = group[group['paperYear'] - group['awardYear'] == 2][['journalID', 'paperYear']]
        y8 = getAveJIFThisYear(journalID_paperYear8, journalID_paperYear_JIF)
        journalID_paperYear9 = group[group['paperYear'] - group['awardYear'] == 3][['journalID', 'paperYear']]
        y9 = getAveJIFThisYear(journalID_paperYear9, journalID_paperYear_JIF)
        journalID_paperYear10 = group[group['paperYear'] - group['awardYear'] == 4][['journalID', 'paperYear']]
        y10 = getAveJIFThisYear(journalID_paperYear10, journalID_paperYear_JIF)
        journalID_paperYear11 = group[group['paperYear'] - group['awardYear'] == 5][['journalID', 'paperYear']]
        y11 = getAveJIFThisYear(journalID_paperYear11, journalID_paperYear_JIF)

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
    fout.close()
    pass


if __name__ == '__main__':
    main()
    pass
