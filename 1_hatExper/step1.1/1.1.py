# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
重新计算jif、paperCnt、h-index
等（hindex是有问题的需要重新处理）

重算paperCnt
"""
import pandas as pd

path = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_affiliationID_sortedName_fieldID_fieldName_" \
       r"paperID_authorID_paperYear_awardYear_citationCnt.txt"
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_paperCnt(11years).txt"
data = pd.read_csv(path, sep='\t', header=None)
data.columns = \
    ['affiliationID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID', 'paperYear', 'awardYear', 'citationCnt']

data = data.groupby(['affiliationID', 'sortedName', 'fieldID', 'fieldName'])

fout = open(pathOut, 'w', encoding='utf-8')

# xi = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for key, group in data:
    y1 = group[group['paperYear']-group['awardYear'] == -5].shape[0]
    y2 = group[group['paperYear'] - group['awardYear'] == -4].shape[0]
    y3 = group[group['paperYear'] - group['awardYear'] == -3].shape[0]
    y4 = group[group['paperYear'] - group['awardYear'] == -2].shape[0]
    y5 = group[group['paperYear'] - group['awardYear'] == -1].shape[0]
    y6 = group[group['paperYear'] - group['awardYear'] == 0].shape[0]
    y7 = group[group['paperYear'] - group['awardYear'] == 1].shape[0]
    y8 = group[group['paperYear'] - group['awardYear'] == 2].shape[0]
    y9 = group[group['paperYear'] - group['awardYear'] == 3].shape[0]
    y10 = group[group['paperYear'] - group['awardYear'] == 4].shape[0]
    y11 = group[group['paperYear'] - group['awardYear'] == 5].shape[0]

    Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11]
    Y = list(map(str, Y))
    fout.write(str(key[0])+'\t'+str(key[1])+'\t'+str(key[2])+'\t'+str(key[3])+'\t'+'\t'.join(Y)+'\n')
fout.close()
