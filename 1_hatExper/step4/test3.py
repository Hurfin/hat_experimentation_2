# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组，已经给各个coAuthor假定好了一个assumeAwardYear，后面是根据各个假定好的awardYear去计算四个参数jif、aveCitation、hIndex、paperCnt

已经算好每个coAuthor的paperCnt, jif, hIndex

算aveCitation（从之前文件里copy过来的，这里citation不除论文数）
"""
import pandas as pd
from collections import defaultdict


def getAveCitaion(refIDs, paperID_set):
    # 查看这一年中所有的被引论文中有多少是这个coAuthor的
    if refIDs is None or len(refIDs) == 0:
        return 0
    citationCnt = 0  # 记录这一年coAuthor的总被引次数
    this_jq_refID_set = set()  # 用来统计这一年这个coAuthor有多少论文被引
    for refID in refIDs:
        if refID in paperID_set:
            this_jq_refID_set.add(refID)
            citationCnt += 1
    if len(this_jq_refID_set) == 0:
        return 0
    # avecitation = citationCnt / len(this_jq_refID_set)
    avecitation = citationCnt
    # avecitation = citationCnt
    return avecitation


path0 = r"E:\FengXu\tmp\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
path1 = r"E:\FengXu\result1\paperID_coAuthorRefID_paperYear.txt"

# fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear	journalID	minYear	maxYear	assumeAwardYear
data1 = pd.read_csv(path0, sep='\t')
# paperID   coAuthorRefID   paperYear
data2 = pd.read_csv(path1, sep='\t')

data1 = data1.astype({'fxID': str, 'coAuthorID': str, 'coAuthorPaperID': str, 'coAuthorPaperYear': int,
                      'journalID': str, 'minYear': int, 'maxYear': int, 'assumeAwardYear': int})
data2 = data2.astype({'paperID': str, 'coAuthorRefID': str, 'paperYear': int})
outer = open(r"E:\FengXu\result1\fxID_assumeAwardYear_minYear_CitationCnt11years(buChuYiLunWenShu).txt", 'w', encoding='utf-8')
data1 = data1.groupby(['fxID', 'assumeAwardYear', 'minYear'])
cnt = 0
for fxID_assumeAwardYear_minYear, group in data1:
    paperID_set = set(list(group['coAuthorPaperID']))  # 这个 coAuthor 的所有年份的论文的id
    fxID_i = fxID_assumeAwardYear_minYear[0]
    assumeAwardYear_i = fxID_assumeAwardYear_minYear[1]
    minYear_i = fxID_assumeAwardYear_minYear[2]

    if cnt%100 == 0:
        print(cnt)
    cnt += 1
    # 这一年被引用的所有的coAuthor的论文id
    refIDs1 = list(data2[data2['paperYear'] - assumeAwardYear_i == -5]['coAuthorRefID'])
    before5 = getAveCitaion(refIDs1, paperID_set)

    refIDs2 = list(data2[data2['paperYear'] - assumeAwardYear_i == -4]['coAuthorRefID'])
    before4 = getAveCitaion(refIDs2, paperID_set)

    refIDs3 = list(data2[data2['paperYear'] - assumeAwardYear_i == -3]['coAuthorRefID'])
    before3 = getAveCitaion(refIDs3, paperID_set)

    refIDs4 = list(data2[data2['paperYear'] - assumeAwardYear_i == -2]['coAuthorRefID'])
    before2 = getAveCitaion(refIDs4, paperID_set)

    refIDs5 = list(data2[data2['paperYear'] - assumeAwardYear_i == -1]['coAuthorRefID'])
    before1 = getAveCitaion(refIDs5, paperID_set)

    refIDs6 = list(data2[data2['paperYear'] - assumeAwardYear_i == 0]['coAuthorRefID'])
    before0 = getAveCitaion(refIDs6, paperID_set)

    refIDs7 = list(data2[data2['paperYear'] - assumeAwardYear_i == 1]['coAuthorRefID'])
    after1 = getAveCitaion(refIDs7, paperID_set)

    refIDs8 = list(data2[data2['paperYear'] - assumeAwardYear_i == 2]['coAuthorRefID'])
    after2 = getAveCitaion(refIDs8, paperID_set)

    refIDs9 = list(data2[data2['paperYear'] - assumeAwardYear_i == 3]['coAuthorRefID'])
    after3 = getAveCitaion(refIDs9, paperID_set)

    refIDs10 = list(data2[data2['paperYear'] - assumeAwardYear_i == 4]['coAuthorRefID'])
    after4 = getAveCitaion(refIDs10, paperID_set)

    refIDs11 = list(data2[data2['paperYear'] - assumeAwardYear_i == 5]['coAuthorRefID'])
    after5 = getAveCitaion(refIDs11, paperID_set)

    cl = [before5, before4, before3, before2, before1, before0, after1, after2, after3, after4, after5]
    cl = list(map(str, cl))
    outer.write(str(fxID_i)+'\t'+str(assumeAwardYear_i)+'\t'+str(minYear_i)+'\t'+'\t'.join(cl)+'\n')
    pass
outer.close()
