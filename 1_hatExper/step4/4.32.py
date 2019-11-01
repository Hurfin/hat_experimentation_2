# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组，已经给各个coAuthor假定好了一个assumeAwardYear，后面是根据各个假定好的awardYear去计算四个参数jif、aveCitation、hIndex、paperCnt

已经算好每个coAuthor的paperCnt, jif

算h-index
首先要搞到 refID_paperYear_thisYearCitationCnt（得先有paperID_refID_paperYear）

上一步已经得到r"E:\FengXu\result1\coAuthorRefID_paperYear_thisYearCitationCnt.txt"

得到r"E:\FengXu\result1\(coAuthor)fxID_hIndex11years.txt"

"""
import pandas as pd
from collections import defaultdict

def h_index(citations):
    citations.sort(reverse=True)
    citations.append(0)
    ans = 0
    for i in range(0, len(citations)):
        if citations[i] < i + 1:
            ans = i
            break
    return ans


def getCitationList(papers, coAuthorRefID_paperYear_thisYearCitationCnt_DF, year):
    papers = papers.drop_duplicates()
    filter_DF = pd.merge(coAuthorRefID_paperYear_thisYearCitationCnt_DF, papers,
                         left_on=['coAuthorRefID'], right_on=['coAuthorPaperID'], how='inner')
    filter_DF = filter_DF[['coAuthorRefID', 'paperYear', 'thisYearCitationCnt']]
    filter_DF = filter_DF[filter_DF['paperYear'] <= year]
    filter_DF = filter_DF.groupby(['coAuthorRefID'])['thisYearCitationCnt'].sum()
    filter_DF = filter_DF.reset_index()
    filter_DF.columns = ['coAuthorRefID', 'citationCntNow']
    return list(filter_DF['citationCntNow'])


path0 = r"E:\FengXu\tmp\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
path1 = r"E:\FengXu\result1\coAuthorRefID_paperYear_thisYearCitationCnt.txt"
# fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear	journalID	minYear	maxYear	assumeAwardYear
data1 = pd.read_csv(path0, sep='\t')
# coAuthorRefID	paperYear	thisYearCitationCnt
data2 = pd.read_csv(path1, sep='\t')
data1 = data1.astype({'fxID': str, 'coAuthorID': str, 'coAuthorPaperID': str, 'coAuthorPaperYear': int,
                      'journalID': str, 'minYear': int, 'maxYear': int, 'assumeAwardYear': int})
data2 = data2.astype({'coAuthorRefID': str, 'paperYear': int, 'thisYearCitationCnt': int})
data1 = data1.groupby(['fxID', 'assumeAwardYear'])
outer = open(r"E:\FengXu\result1\(coAuthor)fxID_hIndex11years.txt", 'w', encoding='utf-8')
for fxID_assumeAwardYear, group in data1:
    fxID_i = fxID_assumeAwardYear[0]
    assumeAwardYear_i = int(fxID_assumeAwardYear[1])
    print(fxID_i, assumeAwardYear_i)
    papers1 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= -5][['coAuthorPaperID']]
    # 论文id、(refID, paperYear, thisYearCitationCnt)、year
    citationList1 = getCitationList(papers1, data2, assumeAwardYear_i - 5)
    hIndex1 = h_index(citationList1)

    papers2 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= -4][['coAuthorPaperID']]
    citationList2 = getCitationList(papers2, data2, assumeAwardYear_i - 4)
    hIndex2 = h_index(citationList2)

    papers3 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= -3][['coAuthorPaperID']]
    citationList3 = getCitationList(papers3, data2, assumeAwardYear_i - 3)
    hIndex3 = h_index(citationList3)

    papers4 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= -2][['coAuthorPaperID']]
    citationList4 = getCitationList(papers4, data2, assumeAwardYear_i - 2)
    hIndex4 = h_index(citationList4)

    papers5 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= -1][['coAuthorPaperID']]
    citationList5 = getCitationList(papers5, data2, assumeAwardYear_i - 1)
    hIndex5 = h_index(citationList5)

    papers6 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= 0][['coAuthorPaperID']]
    citationList6 = getCitationList(papers6, data2, assumeAwardYear_i)
    hIndex6 = h_index(citationList6)

    papers7 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= 1][['coAuthorPaperID']]
    citationList7 = getCitationList(papers7, data2, assumeAwardYear_i + 1)
    hIndex7 = h_index(citationList7)

    papers8 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= 2][['coAuthorPaperID']]
    citationList8 = getCitationList(papers8, data2, assumeAwardYear_i + 2)
    hIndex8 = h_index(citationList8)

    papers9 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= 3][['coAuthorPaperID']]
    citationList9 = getCitationList(papers9, data2, assumeAwardYear_i + 3)
    hIndex9 = h_index(citationList9)

    papers10 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= 4][['coAuthorPaperID']]
    citationList10 = getCitationList(papers10, data2, assumeAwardYear_i + 4)
    hIndex10 = h_index(citationList10)

    papers11 = group[group['coAuthorPaperYear'] - assumeAwardYear_i <= 5][['coAuthorPaperID']]
    citationList11 = getCitationList(papers11, data2, assumeAwardYear_i + 5)
    hIndex11 = h_index(citationList11)

    hl = [hIndex1, hIndex2, hIndex3, hIndex4, hIndex5, hIndex6, hIndex7, hIndex8, hIndex9, hIndex10, hIndex11]
    hl = list(map(str, hl))
    outer.write(str(fxID_i)+'\t'+'\t'.join(hl)+'\n')
    pass
outer.close()