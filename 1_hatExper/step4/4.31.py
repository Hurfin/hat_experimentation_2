# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组，已经给各个coAuthor假定好了一个assumeAwardYear，后面是根据各个假定好的awardYear去计算四个参数jif、aveCitation、hIndex、paperCnt

已经算好每个coAuthor的paperCnt, jif

算h-index
首先要搞到 refID_paperYear_thisYearCitationCnt（得先有paperID_refID_paperYear）

得到r"E:\FengXu\result1\coAuthorRefID_paperYear_thisYearCitationCnt.txt"

"""
import pandas as pd
from collections import defaultdict

path0 = r"E:\FengXu\tmp\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
path1 = r"D:\Dataset\NEW_MAG\Papers.txt"
path2 = r"D:\Dataset\NEW_MAG\PaperReferences.txt"

coAuthorPaperID_set = set()
bool_ = True
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        if bool_ is True:
            bool_ = False
            continue
        line = line.strip('\n').split('\t')
        coAuthorPaperID_set.add(line[2])

paperID_set = set()
outer1 = open(r"E:\FengXu\result1\paperID_refID(refCoAuthor).txt", 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in coAuthorPaperID_set:
            outer1.write(line[0]+'\t'+line[1]+'\n')
            paperID_set.add(line[0])
    pass
outer1.close()
del coAuthorPaperID_set

# find paperID's year
outer2 = open(r"E:\FengXu\result1\paperID_paperYear(paperID_is_refCoAuthorPaper).txt", 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n').split('\t')
        if line[7] is not None and line[7] != '' and line[0] in paperID_set:
            outer2.write(line[0]+'\t'+line[7]+'\n')
outer2.close()
del paperID_set

data1 = pd.read_csv(r"E:\FengXu\result1\paperID_refID(refCoAuthor).txt",
                    sep='\t', header=None, names=['paperID', 'coAuthorRefID'])
data2 = pd.read_csv(r"E:\FengXu\result1\paperID_paperYear(paperID_is_refCoAuthorPaper).txt",
                    sep='\t', header=None, names=['paperID', 'paperYear'])

data = pd.merge(data1, data2, on=['paperID'], how='inner')
del data1, data2
data = data[['paperID', 'coAuthorRefID', 'paperYear']]
data.to_csv(r"E:\FengXu\result1\paperID_coAuthorRefID_paperYear.txt", sep='\t', index=False)

data = data.groupby(['coAuthorRefID', 'paperYear'])['paperID'].count()
data = data.reset_index()
data.columns = ['coAuthorRefID', 'paperYear', 'thisYearCitationCnt']
data.to_csv(r"E:\FengXu\result1\coAuthorRefID_paperYear_thisYearCitationCnt.txt", sep='\t', index=False)
