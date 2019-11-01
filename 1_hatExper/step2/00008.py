# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
除以论文数
"""
import pandas as pd
import os

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sorteName_fieldID_fieldName_aveCitation(11years).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_JIF(11years).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_HIndex(11years).txt"
path4 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_paperCnt(11years).txt"

names1 = ['affID', 'sortedName', 'fieldID', 'fieldName', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']
data_avecitation = pd.read_csv(path1, sep='\t', header=None, names=names1)
names2 = ['affID', 'sortedName', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']
names3 = ['affID', 'sortedName', 'fildID', 'fieldName', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']
data_avejif = pd.read_csv(path2, sep='\t', header=None, names=names2)
data_avehindex = pd.read_csv(path3, sep='\t', header=None, names=names3)
data_avepapercnt = pd.read_csv(path4, sep='\t', header=None, names=names3)

data_avecitation['bf_avecitation'] = data_avecitation.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data_avecitation['af_avecitation'] = data_avecitation.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data_avecitation = data_avecitation.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data_avejif['bf_avejif'] = data_avejif.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data_avejif['af_avejif'] = data_avejif.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data_avejif = data_avejif.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data_avehindex['bf_avehindex'] = data_avehindex.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data_avehindex['af_avehindex'] = data_avehindex.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data_avehindex = data_avehindex.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data_avepapercnt['bf_avepapercnt'] = data_avepapercnt.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data_avepapercnt['af_avepapercnt'] = data_avepapercnt.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data_avepapercnt = data_avepapercnt.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

# data_avecitation, data_avejif, data_avehindex, data_avepapercnt
data = pd.merge(data_avecitation, data_avejif, on=['affID', 'sortedName'], how='left')
data = pd.merge(data, data_avehindex, on=['affID', 'sortedName'], how='inner')
data = pd.merge(data, data_avepapercnt, on=['affID', 'sortedName'], how='inner')

data = data[['affID', 'sortedName', 'fieldID', 'fieldName',
             'bf_avejif', 'bf_avecitation', 'bf_avehindex', 'bf_avepapercnt',
              'af_avejif', 'af_avecitation', 'af_avehindex', 'af_avepapercnt'
             ]]
data = data.fillna(0)
print(data.shape[0])
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_" \
           r"aveJIF_aveCitation_aveHindex_avePaperCnt(before_after5_citationChuYiLunWenShu).txt"
data.to_csv(path_out, sep='\t', index=False)