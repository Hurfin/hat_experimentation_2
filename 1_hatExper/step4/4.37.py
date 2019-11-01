# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算P值，进行分层
r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\filtered_affID_sortedName_fxID_dist.txt"

r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_
bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_af_avejif_af_avecitation_af_avehindex_af_avepapercnt(chuYi).txt"
r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_
bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_af_avejif_af_avecitation_af_avehindex_af_avepapercnt(buChuYi).txt"

r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthorCombined)\(coAuthor)
fxID_assumeAwardYear_minYear_bf_jif_bf_aveCitation_bf_hindex_bf_paperCnt_
af_jif_af_aveCitation_af_hindex_af_paperCnt(chuYiLunWenShu).txt"

最终确定以 1 3 6 的比例去分层
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_" \
        r"bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_" \
        r"af_avejif_af_avecitation_af_avehindex_af_avepapercnt(chuYi).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\4\(coAuthorCombined)\(coAuthor)" \
        r"fxID_assumeAwardYear_minYear_bf_jif_bf_aveCitation_bf_hindex_bf_paperCnt_" \
        r"af_jif_af_aveCitation_af_hindex_af_paperCnt(chuYiLunWenShu).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\filtered_affID_sortedName_fxID_dist.txt"
# affID	sortedName	awardYear	fieldID	fieldName
# bf_avejif	bf_avecitation	bf_avehindex	bf_avepapercnt
# af_avejif	af_avecitation	af_avehindex	af_avepapercnt
data1 = pd.read_csv(path1, sep='\t')
# fxID	assumeAwardYear	minYear
# bf_jif	bf_aveCitation	bf_hindex	bf_paperCnt
# af_jif	af_aveCitation	af_hindex	af_paperCnt
data2 = pd.read_csv(path2, sep='\t')

# affID	sortedName	fxID	dist
data3 = pd.read_csv(path3, sep='\t')
data3 = data3[['affID', 'sortedName', 'fxID']]

data1 = pd.merge(data3, data1, on=['affID', 'sortedName'], how='inner')
data1 = data1.drop(['fxID'], axis=1)
data2 = pd.merge(data3, data2, on=['fxID'], how='inner')
data2 = data2.drop(['affID', 'sortedName'], axis=1)

X = []
Y = []
for i in range(0, len(data1)):
    jif = data1.iloc[i]['bf_avejif']
    citation = data1.iloc[i]['bf_avecitation']
    hindex = data1.iloc[i]['bf_avehindex']
    papercnt = data1.iloc[i]['bf_avepapercnt']
    X.append([jif, citation, hindex, papercnt])
    Y.append(1)

for i in range(0, len(data2)):
    jif = data2.iloc[i]['bf_jif']
    citation = data2.iloc[i]['bf_aveCitation']
    hindex = data2.iloc[i]['bf_hindex']
    papercnt = data2.iloc[i]['bf_paperCnt']
    X.append([jif, citation, hindex, papercnt])
    Y.append(0)

classifier = LogisticRegression()
classifier.fit(X, Y)
pre = classifier.predict_proba(X)
print(pre[:, 1])

cnt1 = 0  # 0-0.1
cnt2 = 0  # 0.1-0.2
cnt3 = 0  # 0.2-0.3
cnt4 = 0  # 0.3-0.4
cnt5 = 0  # 0.4-0.5
cnt6 = 0  # 0.5-0.6
cnt7 = 0  # 0.6-0.7
cnt8 = 0  # 0.7-0.8
cnt9 = 0  # 0.8-0.9
cnt10 = 0  # 0.9-1
for x in pre[:, 1]:
    if 0 <= x < 0.1:
        cnt1 += 1
    if 0.1 <= x < 0.2:
        cnt2 += 1
    if 0.2 <= x < 0.3:
        cnt3 += 1
    if 0.3 <= x < 0.4:
        cnt4 += 1
    if 0.4 <= x < 0.5:
        cnt5 += 1
    if 0.5 <= x < 0.6:
        cnt6 += 1
    if 0.6 <= x < 0.7:
        cnt7 += 1
    if 0.7 <= x < 0.8:
        cnt8 += 1
    if 0.8 <= x < 0.9:
        cnt9 += 1
    if 0.9 <= x <= 1:
        cnt10 += 1
    pass
print("0 <= x < 0.1", cnt1)
print("0.1 <= x < 0.2", cnt2)
print("0.2 <= x < 0.3", cnt3)
print("0.3 <= x < 0.4", cnt4)
print("0.4 <= x < 0.5", cnt5)
print("0.5 <= x < 0.6", cnt6)
print("0.6 <= x < 0.7", cnt7)
print("0.7 <= x < 0.8", cnt8)
print("0.8 <= x < 0.9", cnt9)
print("0.9 <= x <= 1", cnt10)


jqX = []
for i in range(0, len(data1)):
    jif = data1.iloc[i]['bf_avejif']
    citation = data1.iloc[i]['bf_avecitation']
    hindex = data1.iloc[i]['bf_avehindex']
    papercnt = data1.iloc[i]['bf_avepapercnt']
    jqX.append([jif, citation, hindex, papercnt])

coX = []
for i in range(0, len(data2)):
    jif = data2.iloc[i]['bf_jif']
    citation = data2.iloc[i]['bf_aveCitation']
    hindex = data2.iloc[i]['bf_hindex']
    papercnt = data2.iloc[i]['bf_paperCnt']
    coX.append([jif, citation, hindex, papercnt])

pre1 = classifier.predict_proba(jqX)
pre2 = classifier.predict_proba(coX)

print(sum(pre1[:, 1])/len(pre1[:, 1]))
print(sum(pre2[:, 1])/len(pre2[:, 1]))

jie1 = sum(pre1[:, 1])/len(pre1[:, 1])  # jq
jie2 = sum(pre2[:, 1])/len(pre2[:, 1])  # co

cnnt1 = 0
cnnt2 = 0
cnnt3 = 0
for x in pre[:, 1]:
    if x < 0.511445614057:
        cnnt1 += 1
    if 0.511445614057 <= x <= 0.652644669957:
        cnnt2 += 1
    if x > 0.652644669957:
        cnnt3 += 1

print(cnnt1, cnnt2, cnnt3)
l = sorted(pre[:, 1], reverse=True)
print(len(l)*0.1, len(l)*0.4)
print(l)
print(l[int(len(l)*0.1)], l[int(len(l)*0.4)])
# 按1 3 6的比例去划分H M L层
ans_ = []
for i in range(0, len(data1)):  # jieQing
    affID = data1.iloc[i]['affID']
    sortedName = data1.iloc[i]['sortedName']
    awardYear = data1.iloc[i]['awardYear']
    fieldID = data1.iloc[i]['fieldID']
    fieldName = data1.iloc[i]['fieldName']
    jif = data1.iloc[i]['bf_avejif']
    citation = data1.iloc[i]['bf_avecitation']
    hindex = data1.iloc[i]['bf_avehindex']
    papercnt = data1.iloc[i]['bf_avepapercnt']
    pre_i = classifier.predict_proba([[jif, citation, hindex, papercnt]])
    # print(pre_i[:, 1][0])
    prob_ = pre_i[:, 1][0]
    jif_ = data1.iloc[i]['af_avejif']
    citation_ = data1.iloc[i]['af_avecitation']
    hindex_ = data1.iloc[i]['af_avehindex']
    papercnt_ = data1.iloc[i]['af_avepapercnt']
    L = 0; M = 0; H = 0;
    if prob_ < 0.511445614057:
        L = 1
    if 0.511445614057 <= prob_ <= 0.652644669957:
        M = 1
    if 0.652644669957 < prob_:
        H = 1
    xx = [affID, sortedName, awardYear, fieldID, fieldName, jif, citation, hindex, papercnt, L, M, H, jif_, citation_, hindex_, papercnt_]
    xx = list(map(str, xx))
    ans_.append(xx)
    pass
path_out1 = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\1ans\\" + "jq.txt"
fout = open(path_out1, 'w', encoding='utf-8')
fout.write("affID\tsortedName\tawardYear\tfieldID\tfieldName\tbf_jif\tbf_citation\tbf_hindex\tbf_papercnt\tL\tM\tH\taf_jif\taf_citation\taf_hindex\taf_papercnt\n")
for x in ans_:
    fout.write('\t'.join(x)+'\n')
fout.close()


# fxID	assumeAwardYear	minYear
# bf_jif	bf_aveCitation	bf_hindex	bf_paperCnt
# af_jif	af_aveCitation	af_hindex	af_paperCnt
ans__ = []
for i in range(0, len(data2)):  # jieQing
    fxID = data2.iloc[i]['fxID']
    assumeAwardYear = data2.iloc[i]['assumeAwardYear']
    minYear = data2.iloc[i]['minYear']
    jif = data2.iloc[i]['bf_jif']
    citation = data2.iloc[i]['bf_aveCitation']
    hindex = data2.iloc[i]['bf_hindex']
    papercnt = data2.iloc[i]['bf_paperCnt']
    pre_i = classifier.predict_proba([[jif, citation, hindex, papercnt]])
    # print(pre_i[:, 1][0])
    prob_ = pre_i[:, 1][0]
    jif_ = data2.iloc[i]['af_jif']
    citation_ = data2.iloc[i]['af_aveCitation']
    hindex_ = data2.iloc[i]['af_hindex']
    papercnt_ = data2.iloc[i]['af_paperCnt']
    L = 0; M = 0; H = 0;
    if prob_ < 0.511445614057:
        L = 1
    if 0.511445614057 <= prob_ <= 0.652644669957:
        M = 1
    if 0.652644669957 < prob_:
        H = 1
    xx = [fxID, assumeAwardYear, minYear, jif, citation, hindex, papercnt, L, M, H, jif_, citation_, hindex_, papercnt_]
    xx = list(map(str, xx))
    ans__.append(xx)
    pass
path_out2 = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\1ans\\" + "dz.txt"
fout = open(path_out2, 'w', encoding='utf-8')
fout.write("fxID\tassumeAwardYear\tminYear\tbf_jif\tbf_citation\tbf_hindex\tbf_papercnt\tL\tM\tH\taf_jif\taf_citation\taf_hindex\taf_papercnt\n")
for x in ans__:
    fout.write('\t'.join(x)+'\n')
    pass
fout.close()
