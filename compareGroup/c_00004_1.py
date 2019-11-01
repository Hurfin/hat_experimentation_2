# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
逻辑回归，计算P值
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize
path = r'E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\aveCitationCnt_' \
       r'aveJIF_aveH-Index_avePaperCnt_flag.txt'
X = []
y = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('\t')
        flag = float(line[-1])
        attribute = list(map(float, line[:-1]))
        X.append(attribute)
        y.append(flag)
    pass
# X=normalize(X,'l1',0)
classifier = LogisticRegression()
classifier.fit(X, y)
pre = classifier.predict_proba(X)
# print(classifier.classes_)
# print(np.min(pre[:, 1]))
# # print(pre[:, 1])
# print(np.max(pre[:, 1]))







# JQ
path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\JQ_affiliationID_" \
       r"JQ_sortedName_JQ_aveCitationCnt_JQ_aveJIF_JQ_aveH-Index_JQ_avePaperCnt.txt"
JQ = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('\t')
        jq_affiliationID = line[0]
        jq_sortedName = line[1]
        attribute = list(map(float, line[2:]))
        JQ.append([jq_affiliationID, jq_sortedName, attribute])
    pass

# DZ
path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\DZ_authorID_" \
       r"DZ_assumeAwardYear_DZ_aveCitationCnt_DZ_aveJIF_DZ_aveH-Index_DZ_avePaperCnt.txt"
DZ = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('\t')
        DZ_authorID = line[0]
        DZ_assumeAwardYear = line[1]
        attribute = list(map(float, line[2:]))
        DZ.append([DZ_authorID, DZ_assumeAwardYear, attribute])
    pass

fout = open(r'E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\LR_result\JQ_affiliationID_sortedName_P.txt',
            'w', encoding='utf-8')
for jq in JQ:
    p = classifier.predict_proba([jq[2]])[0][1]
    fout.write(jq[0]+'\t'+jq[1]+'\t'+str(p)+'\n')
    pass
fout.close()

fout = open(r'E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\LR_result\DZ_authorID_P.txt',
            'w', encoding='utf-8')
for dz in DZ:
    p = classifier.predict_proba([dz[2]])[0][1]
    fout.write(dz[0]+'\t'+str(p)+'\n')
    pass
fout.close()
