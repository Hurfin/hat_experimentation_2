# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np
from time import time
import os
"""
修改 ，使得所求为，杰青获奖前五年、后五年都存在合作的合作者的CII

r'E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear(Co).txt'
paper id为杰青发表的论文id
从中提取合作者的id
这个也可以得到K(ij)某年份区间内
"""


def main():
    # 先选出参与计算的杰青1210
    path2 = r"E:\FengXu\result\TMP\tmp_data\paperID_authorID_affiliationID_paperYear(Co).txt"
    path5 = r"E:\FengXu\result\TMP\tmp_data\2_affiliationID_authorEnglishNameSorted_minYear_awardYear" \
            r"_academicAge(academicAge5_25).txt"
    path6 = r"E:\FengXu\result\TMP\tmp_data\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_" \
            r"affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_citationCnt.txt"
    # 需要修改上面路径
    path7 = r"E:\FengXu\result\TMP\paperID_authorID_paperYear(coPaperALL).txt"

    names1 = ['affiliationID', 'sortedName', 'awardYear']
    data1 = pd.read_csv(path5, sep='\t', header=None, names=names1, usecols=[0, 1, 3])
    names2 = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'sortedName', 'displayName',
              'chineseName', 'awardYear', 'citationCnt']
    data2 = pd.read_csv(path6, sep='\t', header=None, names=names2)
    data2 = data2[['paperID', 'authorID', 'affiliationID', 'paperYear', 'sortedName']]

    # 杰青发表论文id下的其它作者
    data3 = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'authorID', 'affiliationID', 'paperYear'])
    coAuthorALLPaper_DF = pd.read_csv(path7, sep='\t', header=None,
                                      names=['paperID', 'authorID', 'paperYear'])
    # 首先筛选出这1210个杰青数据
    # 然后把他们按key，groupby，得到一个杰青一个分组
    # 对groupby后的一个分组，对于他的每个paper id，查询在path2中有多少行，那这个论文就有多少个co-author
    # 把co-author数目统计出来（用set保存，使用len），并保留co-author id
    # 前五年完毕后，相同办法算后五年，从中去掉前五年的co-author，查数量

    data = pd.merge(data1, data2, on=['affiliationID', 'sortedName'], how='inner')
    del data1, data2
    data = data[['paperID', 'authorID', 'affiliationID', 'paperYear', 'sortedName', 'awardYear']]

    data = data.groupby(['affiliationID', 'sortedName', 'awardYear'])
    cnt = 0
    pathOut = r"E:\FengXu\result\TMP\JQ_affiliationID_JQ_sortedName_CO_authorID_" \
              r"JQ_awardYear_Ki_Kj_kij_flag(before1_after0).txt"
    fout = open(pathOut, 'w', encoding='utf-8')
    for affID_sortedName_awardYear, group in data:
        cnt += 1
        print('execute JQ ', cnt, 'co-author(before 5 after 5)')
        JQ_affID = affID_sortedName_awardYear[0]
        JQ_sortedName = affID_sortedName_awardYear[1]
        JQ_awardYear = affID_sortedName_awardYear[2]

        # 对于一个杰青，先选出他前五年和后五年的论文
        before5 = \
        group[(-5 <= (group['paperYear'] - group['awardYear'])) & ((group['paperYear'] - group['awardYear']) <= -1)][
            ['paperID']]
        after5 = \
        group[(1 <= (group['paperYear'] - group['awardYear'])) & ((group['paperYear'] - group['awardYear']) <= 5)][
            ['paperID']]
        # 杰青前五年和后五年的论文的id，存起来，后面算和合作者的论文id的交集，即K(ij)
        JQ_before5_paperID_set = set(list(before5['paperID']))
        JQ_after5_paperID_set = set(list(after5['paperID']))

        before5 = before5.drop_duplicates()
        after5 = after5.drop_duplicates()

        JQ_before5_Ki = before5.shape[0]  # 前五年中 CII中的杰青的Ki
        JQ_after5_Ki = after5.shape[0]  # 后五年中 CII中的杰青的Ki

        # 前五年的合作者的author id
        before5_coAuthor = pd.merge(data3, before5, on=['paperID'])[['authorID']]
        # 后五年的合作者的author id
        after5_coAuthor = pd.merge(data3, after5, on=['paperID'])[['authorID']]

        # before5_coAuthor = before5_coAuthor.drop_duplicates()
        # after5_coAuthor = after5_coAuthor.drop_duplicates()  # 有可能包含有前五年的合作者id

        before5_coAuthor_set = set(list(before5_coAuthor['authorID']))
        after5_coAuthor_set = set(list(after5_coAuthor['authorID']))

        del before5_coAuthor, after5_coAuthor

        # after5_coAuthor_set -= before5_coAuthor_set  # 去除后五年中前五年出现过的合作者
        #
        # """ before5_coAuthor_set前五年所有合作者id，after5_coAuthor_set后五年所有合作者id """
        #
        # collaborators_before = list(before5_coAuthor_set)
        # collaborators_after = list(after5_coAuthor_set)

        # 修改此处，使得所求为，杰青获奖前五年、后五年都存在合作的合作者的author id
        collaborators_before = list(before5_coAuthor_set & after5_coAuthor_set)
        collaborators_after = list(before5_coAuthor_set & after5_coAuthor_set)

        # 前五年的每个合作者
        start = time()
        for collaborators_i in collaborators_before:
            co_i_allPapers = coAuthorALLPaper_DF[coAuthorALLPaper_DF['authorID'] == collaborators_i]  # 找到这个合作者的所有论文
            co_i_beforePapers = co_i_allPapers[(-5 <= (co_i_allPapers['paperYear'] - JQ_awardYear)) & (
                (co_i_allPapers['paperYear'] - JQ_awardYear) <= -1)]['paperID']  # 前五年的论文

            co_i_beforePapers_set = set(list(co_i_beforePapers))

            CO_before5_Kj = len(co_i_beforePapers_set)

            JQ_CO_before5_KIJ = len(JQ_before5_paperID_set & co_i_beforePapers_set)

            fout.write(str(JQ_affID) + '\t' + str(JQ_sortedName) + '\t' + str(collaborators_i) + '\t' + str(
                JQ_awardYear) + '\t' + str(JQ_before5_Ki) + '\t' + str(CO_before5_Kj) + '\t' + str(
                JQ_CO_before5_KIJ) + '\t' + str(1) + '\n')

        end = time()
        print("before 5 years is ok ", end-start)

        # 后五年的每个合作者
        start = time()
        for collaborators_i in collaborators_after:
            co_i_allPapers = coAuthorALLPaper_DF[coAuthorALLPaper_DF['authorID'] == collaborators_i]  # 找到这个合作者的所有论文
            co_i_afterPapers = co_i_allPapers[
                (1 <= (co_i_allPapers['paperYear'] - JQ_awardYear)) & ((co_i_allPapers['paperYear'] - JQ_awardYear) <= 5)][
                'paperID']  # 后五年的论文

            co_i_afterPapers_set = set(list(co_i_afterPapers))

            CO_after5_Kj = len(co_i_afterPapers_set)

            JQ_CO_after5_KIJ = len(JQ_after5_paperID_set & co_i_afterPapers_set)

            fout.write(str(JQ_affID) + '\t' + str(JQ_sortedName) + '\t' + str(collaborators_i) + '\t' + str(
                JQ_awardYear) + '\t' + str(JQ_after5_Ki) +
                       '\t' + str(CO_after5_Kj) + '\t' + str(JQ_CO_after5_KIJ) + '\t' + str(0) + '\n')
            pass
        end = time()
        print("after 5 years is ok ", end-start)
    fout.close()


if __name__ == '__main__':
    main()
