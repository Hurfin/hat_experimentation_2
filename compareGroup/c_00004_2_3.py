# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
# path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dataMerge.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dz_" \
        r"DZ_authorID_aveCitationCnt_aveJIF_aveH-Index_avePaperCnt_L_M_H_award.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\jq_" \
        r"JQ_affiliationID_JQ_sortedName_aveCitationCnt_aveJIF_aveH-Index_avePaperCnt_L_M_H_award.txt"
dzNames = ['DZ_authorID', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']
data1 = pd.read_csv(path1, sep='\t', header=None, names=dzNames)
jqNames = ['JQ_affiliation', 'JQ_sortedName', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'S1', 'S2', 'S3', 'award']
data2 = pd.read_csv(path2, sep='\t', header=None, names=jqNames)

data1['S1'] = data1.apply(lambda x: 0, axis=1)
data1['S2'] = data1.apply(lambda x: 0, axis=1)
data1['S3'] = data1.apply(lambda x: 0, axis=1)

data2['L'] = data2.apply(lambda x: 0, axis=1)
data2['M'] = data2.apply(lambda x: 0, axis=1)
data2['H'] = data2.apply(lambda x: 0, axis=1)

data1 = data1.set_index(['DZ_authorID'])
data2 = data2.set_index(['JQ_affiliation', 'JQ_sortedName'])

data = pd.concat([data1, data2], axis=0)
# print(data.sample(10))
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dataMerge2(forSi).txt"
data.to_csv(pathOut, sep='\t')
del data1, data2


model1 = LinearRegression()
model1.fit(data[['L', 'M', 'H', 'S1', 'S2', 'S3']], data[['aveCitationCnt']])
ans1 = model1.coef_[0]

model2 = LinearRegression()
model2.fit(data[['L', 'M', 'H', 'S1', 'S2', 'S3']], data[['aveJIF']])
ans2 = model2.coef_[0]

model3 = LinearRegression()
model3.fit(data[['L', 'M', 'H', 'S1', 'S2', 'S3']], data[['aveH-Index']])
ans3 = model3.coef_[0]

model4 = LinearRegression()
model4.fit(data[['L', 'M', 'H', 'S1', 'S2', 'S3']], data[['avePaperCnt']])
ans4 = model4.coef_[0]

pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\linearRegression_ans2.txt"

ans_DF = pd.DataFrame([ans1, ans2, ans3, ans4], index=['aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt'], columns=['L', 'M', 'H', 'S1', 'S2', 'S3'])

ans_DF.to_csv(pathOut, sep='\t')

print(ans1, 'aveCitationCnt')
print(ans2, 'aveJIF')
print(ans3, 'aveH-Index')
print(ans4, 'avePaperCnt')
