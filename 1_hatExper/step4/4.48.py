# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算dz合作密度
r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"
r"E:\FengXu\tmp\dz_" \
r"fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"

"""
import pandas as pd
import sys

def getCoFxIDs(paperIDs, dzPaperID_cofxIDs_dict):
    # input 对照组的paperIDs
    # return 为这些paperID下找到的coAuthor们的fxID
    paperIDs = list(paperIDs)
    ans_ = set()
    for x in paperIDs:
        if x not in dzPaperID_cofxIDs_dict.keys():
            continue
        try:
            ans_ |= dzPaperID_cofxIDs_dict[x]
        except:
            print(x, "error")
            sys.exit(0)
    return ans_


# dz data
path0 = r"E:\FengXu\tmp\dz_" \
        r"fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
# dz coAuthor data
path1 = r"E:\FengXu\result3\dzCoFxID_dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"  # 考虑设置fxID
# 需要dz组的合作者的全部论文信息（paperID、paperYear、以及paperID对应的合作者的authorID）
path2 = r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID_dzCoFxID_PYear.txt"  # 需要加上和dzCoAuthorID对应的fxID
dzPaperID_cofxIDs_dict = dict()  # key为dzPaperID，value为该paperID下dz组的coAuthor们的fxID
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] not in dzPaperID_cofxIDs_dict.keys():
            dzPaperID_cofxIDs_dict[line[1]] = set()
        dzPaperID_cofxIDs_dict[line[1]].add(line[0])
        pass
    pass
data2 = pd.read_csv(path2, sep='\t', header=None,
                    names=['dzCoCoPaperID', 'dzCoAuthorID', 'dzCoFxID', 'PYear'])
data2 = data2.astype({'dzCoCoPaperID': str, 'dzCoAuthorID': str, 'dzCoFxID': str, 'PYear': int})
data2 = data2.groupby(['dzCoFxID'])
dzCoFxID_group_dict = dict()  # key为对照组的coAuthor的fxID，value为该fxID下的所有数据（包含的列见data2的列名）
for dzCoFxID_i, group in data2:
    dzCoFxID_group_dict[dzCoFxID_i] = group


data1 = pd.read_csv(path0, sep='\t', header=None,
                    names=['fxID', 'coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear', 'journalID', 'minYear',
                           'maxYear', 'assumeAwardYear'])
data1 = data1.astype({'fxID': str, 'coAuthorID': str, 'coAuthorPaperID': str, 'coAuthorPaperYear': int,
                      'journalID': str, 'minYear': int, 'maxYear': int, 'assumeAwardYear': int})

data1 = data1.groupby(['fxID', 'assumeAwardYear'])
fout1 = open(r"E:\FengXu\result3\dzFxID_assumeAwardYear_dzCoFxID_CIIBF_CIIAF.txt", 'w', encoding='utf-8')
fout2 = open(r"E:\FengXu\result3\dzFxID_assumeAwardYear_aveCIIBF_aveCIIAF.txt", 'w', encoding='utf-8')
fout1.write("dzFxID\tdzAssumeAwardYear\tdzCoFxID\tCIIBF\tCIIAF\n")
fout2.write("dzFxID\tdzAssumeAwardYear\taveCIIBF\taveCIIAF\n")
CC = 0
for k, group in data1:
    print(CC)
    CC += 1
    fxID_i = k[0]
    assumeAwardYear_i = k[1]
    dzPaperIDs_BF = set(list(group[(group['coAuthorPaperYear'] - assumeAwardYear_i >= -5) & (
        group['coAuthorPaperYear'] - assumeAwardYear_i <= -1)]['coAuthorPaperID']))
    dzPaperIDs_AF = set(list(group[(group['coAuthorPaperYear'] - assumeAwardYear_i >= 1) & (
        group['coAuthorPaperYear'] - assumeAwardYear_i <= 5)]['coAuthorPaperID']))

    ki_BF = len(dzPaperIDs_BF)
    ki_AF = len(dzPaperIDs_AF)

    fxIDsBF = getCoFxIDs(dzPaperIDs_BF, dzPaperID_cofxIDs_dict)  # 通过paperID list找到对应的coAuthor list
    fxIDsAF = getCoFxIDs(dzPaperIDs_AF, dzPaperID_cofxIDs_dict)
    intersection_BF_AF = fxIDsBF & fxIDsAF  # 找到前后都有合作的coAuthor list

    sumCIIBF = 0
    sumCIIAF = 0
    cnt = 0
    for dzCofxID_k in list(intersection_BF_AF):  # 对于每个coAuthor，计算pair CII
        if dzCofxID_k not in dzCoFxID_group_dict.keys():
            continue
        # 取出该fxID对应的分组数据
        group_k = dzCoFxID_group_dict[dzCofxID_k]
        fxID_k_BF_paperIDs = set(list(group_k[(group_k['PYear'] - assumeAwardYear_i >= -5) &
                                              (group_k['PYear'] - assumeAwardYear_i <= -1)]['dzCoCoPaperID']))
        fxID_k_AF_paperIDs = set(list(group_k[(group_k['PYear'] - assumeAwardYear_i >= 1) &
                                              (group_k['PYear'] - assumeAwardYear_i <= 5)]['dzCoCoPaperID']))

        kj_BF = len(fxID_k_BF_paperIDs)
        kj_AF = len(fxID_k_AF_paperIDs)

        kij_BF = len(dzPaperIDs_BF & fxID_k_BF_paperIDs)
        kij_AF = len(dzPaperIDs_AF & fxID_k_AF_paperIDs)

        CIIBF = 0
        CIIAF = 0
        if kij_BF != 0 and ki_BF != 0 and kj_BF != 0:
            CIIBF = kij_BF / (ki_BF * kj_BF)
        if kij_AF != 0 and ki_AF != 0 and kj_AF != 0:
            CIIAF = kij_AF / (ki_AF * kj_AF)

        fout1.write(fxID_i + '\t' + str(assumeAwardYear_i) + '\t' + dzCofxID_k + '\t' + str(CIIBF) + '\t' + str(CIIAF) + '\n')
        print(fxID_i + '\t' + str(assumeAwardYear_i) + '\t' + dzCofxID_k + '\t' + str(CIIBF) + '\t' + str(CIIAF))
        cnt += 1
        sumCIIBF += CIIBF
        sumCIIAF += CIIAF
        pass
    aveCIIBF = 0
    aveCIIAF = 0
    if sumCIIBF != 0:
        aveCIIBF = sumCIIBF / cnt
    if sumCIIAF != 0:
        aveCIIAF = sumCIIAF / cnt
    fout2.write(fxID_i + '\t' + str(assumeAwardYear_i) + '\t' + str(aveCIIBF) + '\t' + str(aveCIIAF) + '\n')
    print(aveCIIBF, aveCIIAF)
    pass
fout1.close()
fout2.close()
