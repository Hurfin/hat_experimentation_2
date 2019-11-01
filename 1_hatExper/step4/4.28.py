# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已经有了
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\JIF\(all)journalID_JIF_perYear_from1989to2017.txt"

r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author
(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"

开始找对照组的人了

首先给每个coAuthor一个假定的awardYear（基本原则是和jq的minPaperYear相同的就随机从这些jq的awardYear中随机的选一个）
（需要注意的是jq中的minYear有些年份是没有的，所以这一步，有些coAuthor由于他们的minYear在jq中没有对应的，所以就直接删掉这些人了）
"""
import pandas as pd
import csv
import random
# path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\JIF\(all)journalID_JIF_perYear_from1989to2017.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"
# names = ['journalID'] + [str(i) for i in range(1989, 2018)]
# data1 = pd.read_csv(path1, sep='\t', header=None, names=names)
# fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear	journalID	minYear	maxYear
data2 = pd.read_csv(path2, sep='\t')
data2 = data2.astype({'fxID': str, 'coAuthorID': str, 'coAuthorPaperID': str, 'coAuthorPaperYear': int,
                      'journalID': str, 'minYear': int, 'maxYear': int})
# print(data1.shape[0])
print(data2.shape[0])
print(data2[['fxID']].drop_duplicates().shape[0])
print(set(list(data2['minYear'])))
# 要给co-author一个假定的award year

# 看下各个杰青的对应各个minYear的awardYear都有哪些
# affID	sortedName	awardYear	fieldID	fieldName	minPaperYear	maxPaperYear
path_jq = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq\new_data\new_filter_jqRemain929.txt"
data_jq = pd.read_csv(path_jq, sep='\t')
minYear_awardYears = dict()
for i in range(0, len(data_jq)):
    minYear = data_jq.iloc[i]['minPaperYear']
    awardYear = data_jq.iloc[i]['awardYear']
    if minYear not in minYear_awardYears.keys():
        minYear_awardYears[minYear] = set()
    minYear_awardYears[int(minYear)].add(int(awardYear))
    pass
minYear_awardYears = sorted(minYear_awardYears.items(), key=lambda x: x[0])
jq_minYear_awardYears = dict()
# 查看了下jq的minYear对应哪些awardYear
for k, v in minYear_awardYears:
    print(k, list(v))
    jq_minYear_awardYears[k]=list(v)
    pass


data3 = data2[['fxID', 'minYear']]
data3 = data3.drop_duplicates()

path_out_tmp = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\3\tmp\fxID_minYear_assumeAwardYear.txt"
path_out1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_" \
           r"journalID_minYear_maxYear_assumeAwardYear.txt"


jq_minYears = [1980, 1981, 1982, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995,
               1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]

# data3['assumeAwardYear'] = data3.apply(lambda x: random.choice(jq_minYear_awardYears[x['minYear']]), axis=1)

# data = pd.merge(data2, data3, on=['fxID'], how='inner')

# outer = open(path_out, 'w', encoding='utf-8')
# outer.write("fxID\tcoAuthorID\tcoAuthorPaperID\tcoAuthorPaperYear\tjournalID\tminYear\tmaxYear\tassumeAwardYear"+'\n')
outer_tmp = open(path_out_tmp, 'w', encoding='utf-8')
outer_tmp.write("fxID\tminYear\tassumeAwardYear\n")
for i in range(len(data3)):
    if int(data3.iloc[i]['minYear']) not in jq_minYears:
        continue
    assumeAwardYear = random.choice(jq_minYear_awardYears[int(data3.iloc[i]['minYear'])])
    outer_tmp.write(str(data3.iloc[i]['fxID'])+'\t'+str(data3.iloc[i]['minYear'])+'\t'+str(assumeAwardYear)+'\n')
    pass
outer_tmp.close()
# data2.to_csv(path_out, sep='\t', index=None)
data3 = pd.read_csv(path_out_tmp, sep='\t')
data3 = data3.astype({'fxID': str, 'minYear': int, 'assumeAwardYear': int})
data3 = data3[['fxID', 'assumeAwardYear']]
print(data2.columns, data3.columns)

data = pd.merge(data2, data3, on=['fxID'], how='inner')
data = data[['fxID', 'coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear', 'journalID', 'minYear', 'maxYear', 'assumeAwardYear']]

data.to_csv(path_out1, sep='\t', index=False)
