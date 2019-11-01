# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
拟合
"""
import pandas as pd
import numpy as np
jqpath = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\jq_JQ_affiliationID_" \
         r"JQ_sortedName_aveCitationCnt_aveJIF_aveH-Index_avePaperCnt_L_M_H_award.txt"
dzpath = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dz_DZ_authorID_" \
         r"aveCitationCnt_aveJIF_aveH-Index_avePaperCnt_L_M_H_award.txt"

JQnames = ['JQ_affiliationID', 'JQ_sortedName', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']
DZnames = ['DZ_authorID', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']

JQ = pd.read_csv(jqpath, sep='\t', header=None, names=JQnames, index_col=['JQ_affiliationID', 'JQ_sortedName'])
DZ = pd.read_csv(dzpath, sep='\t', header=None, names=DZnames, index_col=['DZ_authorID'])

JQ = JQ[['aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']]
DZ = DZ[['aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']]

data = pd.concat([JQ, DZ], axis=0)
# data.reset_index()
# print(data.sample(10))
"""  数据存档 """
data.to_csv(r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dataMerge.txt", sep='\t')

