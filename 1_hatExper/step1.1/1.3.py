# -*- coding: utf-8 -*-
"""
E:\pythonCode\RJ_experimentation_1\Data_1\ref\refID_paperYear_thisYearCitationCnt.txt
重新计算hindex
"""
# !/usr/bin/env python
import pandas as pd
import csv
import os
import numpy as np


def h_index(citations):
    citations.sort(reverse=True)
    citations.append(0)
    ans = 0
    for i in range(0, len(citations)):
        if citations[i] < i + 1:
            ans = i
            break
    return ans


def getCitationList(PID_DF, year, refID_paperYear_thisYearCitationCnt):
    """得到截止到这一年为止的所有论文的citation list"""
    PID_DF = PID_DF.drop_duplicates()
    refID_paperYear_thisYearCitationCnt = pd.merge(refID_paperYear_thisYearCitationCnt, PID_DF, left_on=['refID'],
                                                   right_on=['paperID'], how='inner')
    refID_paperYear_thisYearCitationCnt = refID_paperYear_thisYearCitationCnt[['refID', 'paperYear', 'thisYearCitationCnt']]
    refID_paperYear_thisYearCitationCnt = refID_paperYear_thisYearCitationCnt[
        refID_paperYear_thisYearCitationCnt['paperYear'] <= year]
    refID_citationCnt_now = refID_paperYear_thisYearCitationCnt.groupby(['refID'])['thisYearCitationCnt'].sum()
    refID_citationCnt_now = refID_citationCnt_now.reset_index()
    refID_citationCnt_now.columns = ['refID', 'citationCntNow']
    return list(refID_citationCnt_now['citationCntNow'])


def main():
    path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_affiliationID_sortedName_fieldID_fieldName_paperID_" \
            r"authorID_paperYear_awardYear_citationCnt.txt"
    path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\ref\refID_paperYear_thisYearCitationCnt.txt"

    path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_HIndex(11years).txt"
    refID_paperYear_thisYearCitationCnt = pd.read_csv(path2, sep='\t', header=None,
                                                      names=['refID', 'paperYear', 'thisYearCitationCnt'])

    refID_paperYear_thisYearCitationCnt = refID_paperYear_thisYearCitationCnt.astype(
        {'refID': str, 'paperYear': int, 'thisYearCitationCnt': int}
    )
    data = pd.read_csv(path1, sep='\t', header=None)
    data.columns = ['affiliationID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID',  'paperYear',
                    'awardYear', 'citationCnt']
    data = data.astype(
        {'affiliationID': str, 'sortedName': str, 'fieldID': str, 'fieldName': str, 'paperID': str, 'authorID': str,
         'paperYear': int, 'awardYear': int, 'citationCnt': int}
    )
    data = data.groupby(['affiliationID', 'sortedName', 'fieldID', 'fieldName', 'awardYear'])
    fout = open(path_out, 'w', encoding='utf-8')
    for key, group in data:
        PID_DF = group[group['paperYear'] - group['awardYear'] <= -5][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]-5, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y1 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= -4][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]-4, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y2 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= -3][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]-3, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y3 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= -2][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]-2, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y4 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= -1][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]-1, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y5 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= 0][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4], refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y6 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= 1][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]+1, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y7 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= 2][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]+2, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y8 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= 3][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]+3, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y9 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= 4][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]+4, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y10 = h_index(citationList)

        PID_DF = group[group['paperYear'] - group['awardYear'] <= 5][['paperID']]  # 截至这一年，已经发表的论文总的id
        citationList = getCitationList(PID_DF, key[4]+5, refID_paperYear_thisYearCitationCnt)  # 得到截至这一年，已经发表过的所有论文的当前引用量
        y11 = h_index(citationList)

        Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11]
        Y = list(map(str, Y))

        fout.write(str(key[0]) + '\t' + str(key[1]) + '\t' + str(key[2]) + '\t' + str(key[3]) + '\t' + '\t'.join(Y) + '\n')
        pass
    fout.close()
    pass


if __name__ == '__main__':
    main()
