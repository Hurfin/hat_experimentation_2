# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
重新计算jif、paperCnt、h-index
等（hindex是有问题的需要重新处理）

重算jif
"""

import pandas as pd
from collections import defaultdict

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
    path = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_affiliationID_sortedName_" \
           r"fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
    path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
            r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
            r"awardYear_citationCnt_journalID.txt"
    path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_JIF(11years).txt"

    data_tmp = pd.read_csv(path, sep='\t', header=None, names=['affiliationID', 'sortedName', 'fieldID', 'fieldName',
                                                               'paperID', 'authorID', 'paperYear', 'awardYear',
                                                               'citationCnt'])
    data_tmp = data_tmp[['paperID']]
    data_tmp = data_tmp.drop_duplicates()

    data = pd.read_csv(path1, sep='\t', header=None)
    data.columns = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
                    'chineseName', 'awardYear', 'citationCnt', 'journalID']
    data = pd.merge(data, data_tmp, on=['paperID'], how='inner')
    xx = ['affiliationID', 'sortedName', 'authorID', 'paperID', 'paperYear', 'awardYear',
          'citationCnt', 'journalID']
    data = data[
        xx
    ]
    data = data[data['awardYear'] <= 2013]
    data = data.groupby(['affiliationID', 'sortedName'])
    journalID_paperYear_JIF = getJournalJIF()
    fout = open(path_out, 'w', encoding='utf-8')
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

        Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11]
        Y = list(map(str, Y))
        fout.write(str(key[0]) + '\t' + str(key[1]) + '\t' + '\t'.join(Y) + '\n')
    fout.close()
    pass


if __name__ == '__main__':
    main()
    pass
