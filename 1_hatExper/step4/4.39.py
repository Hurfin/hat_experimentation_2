# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算合作密度
"""
import pandas as pd
import os
def getCoFxIDs(paperIDs, jqPaperID_fxIDs_dict):
    paperIDs = list(paperIDs)
    ans_ = set()
    for x in paperIDs:
        if x not in jqPaperID_fxIDs_dict.keys():
            continue
        ans_ |= jqPaperID_fxIDs_dict[x]
    return ans_

path0 = r"E:\FengXu\tmp\JQ_affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
path1 = r"E:\FengXu\result2\fxID_coAuthorPaperID_coAuthorID_coPaperYear.txt"
path2 = r"E:\FengXu\tmp\fxID_jqPaperID_coAuthorID_affID_normalizedName(coAuthorIndex).txt"
# affID sortedName  fieldID fieldName   paperID authorID    paperYear   awardYear   citationCnt
data1 = pd.read_csv(path0, sep='\t')
data1 = data1.astype({'affID': str, 'sortedName': str, 'fieldID': str, 'fieldName': str, 'paperID': str, 'authorID': str,
                      'paperYear': int, 'awardYear': int, 'citationCnt': int})
jqPaperID_fxIDs_dict = dict()  # 一个杰青的paperID下对应的coAuthor的fxID
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] not in jqPaperID_fxIDs_dict.keys():
            jqPaperID_fxIDs_dict[line[1]] = set()
        jqPaperID_fxIDs_dict[line[1]].add(line[0])
        pass
    pass

fxID_group_dict = dict()
data2 = pd.read_csv(path1, sep='\t', header=None, names=['fxID', 'coAuthorPaperID', 'coAuthorID', 'coPaperYear'])
data2 = data2.astype({'fxID': str, 'coAuthorPaperID': str, 'coAuthorID': str, 'coPaperYear': int})
data2 = data2.groupby(['fxID'])
for k, group in data2:
    # print(type(k))
    fxID_group_dict[k] = group

data1 = data1.groupby(['affID', 'sortedName', 'awardYear'])
fout1 = open(r"E:\FengXu\result2\affID_sortedName_fxID_CIIBF_CIIAF.txt", 'w', encoding='utf-8')
fout2 = open(r"E:\FengXu\result2\affID_sortedName_aveCIIBF_aveCIIAF.txt", 'w', encoding='utf-8')
fout1.write("affID\tsortedName\tfxID\tCIIBF\tCIIAF\n")
fout2.write("affID\tsortedName\taveCIIBF\taveCIIAF\n")
CC = 0
for k, group in data1:
    print(CC)
    CC += 1
    affID_i = k[0]
    sortedName_i = k[1]
    awardYear_i = k[2]
    paperIDsBF = set(list(group[(-5 <= (group['paperYear'] - awardYear_i)) & ((group['paperYear'] - awardYear_i) <= -1)]['paperID']))
    paperIDsAF = set(list(group[(1 <= (group['paperYear'] - awardYear_i)) & ((group['paperYear'] - awardYear_i) <= 5)]['paperID']))

    fxIDsBF = getCoFxIDs(paperIDsBF, jqPaperID_fxIDs_dict)  # 得到他们coAuthor们的fxID
    fxIDsAF = getCoFxIDs(paperIDsAF, jqPaperID_fxIDs_dict)  #

    ki_BF = len(paperIDsBF)
    ki_AF = len(paperIDsAF)

    intersection_BF_AF = fxIDsBF & fxIDsAF
    # print(len(intersection_BF_AF))
    # print("intersect Num:", len(intersection_BF_AF))

    sumCIIBF = 0
    sumCIIAF = 0
    cnt = 0
    for fxID_k in list(intersection_BF_AF):
        if fxID_k not in fxID_group_dict.keys():
            continue
        group_k = fxID_group_dict[fxID_k]  # 得到该fxID对应的所有论文
        # print("OK")

        # 'fxID', 'coAuthorPaperID', 'coAuthorID', 'coPaperYear'
        fxID_k_BF_paperIDs = set(list(group_k[(-5 <= (group_k['coPaperYear'] - awardYear_i)) & ((group_k['coPaperYear'] - awardYear_i) <= -1)]['coAuthorPaperID']))
        fxID_k_AF_paperIDs = set(list(group_k[(1 <= (group_k['coPaperYear'] - awardYear_i)) & ((group_k['coPaperYear'] - awardYear_i) <= 5)]['coAuthorPaperID']))

        kj_BF = len(fxID_k_BF_paperIDs)
        kj_AF = len(fxID_k_AF_paperIDs)

        kij_BF = len(paperIDsBF & fxID_k_BF_paperIDs)
        kij_AF = len(paperIDsAF & fxID_k_AF_paperIDs)
        # print(kj_BF, kj_AF, kij_BF, kij_AF)

        CIIBF = 0
        CIIAF = 0
        if kij_BF != 0 and ki_BF != 0 and kj_BF != 0:
            CIIBF = kij_BF / (ki_BF * kj_BF)
        if kij_AF != 0 and ki_AF != 0 and kj_AF != 0:
            CIIAF = kij_AF / (ki_AF * kj_AF)
        fout1.write(affID_i+'\t'+sortedName_i+'\t'+fxID_k+'\t'+str(CIIBF)+'\t'+str(CIIAF)+'\n')
        print(affID_i+'\t'+sortedName_i+'\t'+fxID_k+'\t'+str(CIIBF)+'\t'+str(CIIAF))
        cnt += 1
        sumCIIBF += CIIBF
        sumCIIAF += CIIAF
    aveCIIBF = 0
    aveCIIAF = 0
    if sumCIIBF != 0:
        aveCIIBF = sumCIIBF / cnt
    if sumCIIAF != 0:
        aveCIIAF = sumCIIAF / cnt
    fout2.write(affID_i+'\t'+sortedName_i+'\t'+str(aveCIIBF)+'\t'+str(aveCIIAF)+'\n')
    print(aveCIIBF, aveCIIAF)
    pass
fout1.close()
fout2.close()
