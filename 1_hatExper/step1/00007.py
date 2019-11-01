# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已经有了paper id， ref id, paper year
计算avecitation（引用量除以论文数）
"""
import pandas as pd
import numpy as np

def getAveCitaion(refIDs, paperID_set):
    # 查看这一年中所有的被引论文中有多少是这个杰青的
    if refIDs is None or len(refIDs) == 0:
        return 0
    citationCnt = 0  # 记录这一年杰青的总被引次数
    this_jq_refID_set = set()  # 用来统计这一年这个杰青有多少论文被引
    for refID in refIDs:
        if refID in paperID_set:
            this_jq_refID_set.add(refID)
            citationCnt += 1
    if len(this_jq_refID_set) == 0:
        return 0
    avecitation = citationCnt / len(this_jq_refID_set)
    return avecitation

path0 = r"E:\FengXu\result1\paperID_refID_paperYear(refJQ).txt"
path1 = r"E:\FengXu\tmp\JQ_" \
        r"affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"

names1 = ['paperID', 'refID', 'paperYear']
names2 = ['affID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID', 'paperYear', 'awardYear', 'citationCnt']

data1 = pd.read_csv(path0, sep='\t', header=None, names=names1)
data2 = pd.read_csv(path1, sep='\t', header=None, names=names2)
colType1 = {'paperID': str, 'refID': str ,'paperYear': int}
colType2 = {'affID': str, 'sortedName': str, 'fieldID': str, 'fieldName': str, 'paperID': str,
            'authorID': str, 'paperYear': int, 'awardYear': int, 'citationCnt': int}
data1 = data1.astype(colType1)
data2 = data2.astype(colType2)
data2 = data2.groupby(['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName'])

pathOut = r"E:\FengXu\result1\affID_sorteName_fieldID_fieldName_aveCitation(11years).txt"
outer = open(pathOut, 'w', encoding='utf-8')
for key, group in data2:
    paperID_set = set(list(group['paperID']))  # 这个杰青的所有年份的论文的id
    awardYear = key[2]
    # 这一年被引用的所有杰青的论文的id
    refIDs = list(data1[data1['paperYear'] - awardYear == -5]['refID'])
    before5 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == -4]['refID'])
    before4 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == -3]['refID'])
    before3 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == -2]['refID'])
    before2 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == -1]['refID'])
    before1 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == 0]['refID'])
    after0 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == 1]['refID'])
    after1 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == 2]['refID'])
    after2 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == 3]['refID'])
    after3 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == 4]['refID'])
    after4 = getAveCitaion(refIDs, paperID_set)

    refIDs = list(data1[data1['paperYear'] - awardYear == 5]['refID'])
    after5 = getAveCitaion(refIDs, paperID_set)

    x = str(key[0])+'\t'+str(key[1])+'\t'+str(key[3])+'\t'+str(key[4])+'\t'+ '\t'.join(
        list(map(str, [before5, before4, before3, before2, before1, after0, after1, after2, after3, after4, after5]))
    ) + '\n'
    outer.write(x)
outer.close()
