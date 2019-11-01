# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
按P值进行分组
可以把0.6以下算作低概率 0.6-0.9算作中概率 0.9-1算作高概率
L   p<0.6
M   0.6<=p<0.9
H    P>=0.9
"""
import pandas as pd
import numpy as np

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\LR_result(beforeAward5years)\DZ_authorID_P.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\LR_result(beforeAward5years)\JQ_affiliationID_" \
        r"sortedName_P.txt"

path11 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\DZ_authorID_" \
         r"DZ_assumeAwardYear_DZ_aveCitationCnt_DZ_aveJIF_DZ_aveH-Index_DZ_avePaperCnt(afterAward5Years).txt"
path22 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\JQ_affiliationID_" \
         r"JQ_sortedName_JQ_aveCitationCnt_JQ_aveJIF_JQ_aveH-Index_JQ_avePaperCnt(afterAward5Years).txt"

""" 先给各个人确认是属于哪个分组（L\M\H） """
DZ1 = pd.read_csv(path1, sep='\t', header=None, names=['DZ_authorID', 'DZ_P'])
JQ1 = pd.read_csv(path2, sep='\t', header=None, names=['JQ_affiliationID', 'JQ_sortedName', 'JQ_P'])

DZ1['L'] = DZ1.apply(lambda x: 1 if (x['DZ_P'] < 0.6) else 0, axis=1)
DZ1['M'] = DZ1.apply(lambda x: 1 if (0.6 <= x['DZ_P'] < 0.9) else 0, axis=1)
DZ1['H'] = DZ1.apply(lambda x: 1 if (0.9 <= x['DZ_P'] <= 1) else 0, axis=1)
DZ1['award'] = DZ1.apply(lambda x: 0, axis=1)
# print(DZ1.sample(10))

JQ1['L'] = JQ1.apply(lambda x: 1 if (x['JQ_P'] < 0.6) else 0, axis=1)
JQ1['M'] = JQ1.apply(lambda x: 1 if (0.6 <= x['JQ_P'] < 0.9) else 0, axis=1)
JQ1['H'] = JQ1.apply(lambda x: 1 if (0.9 <= x['JQ_P'] <= 1) else 0, axis=1)
JQ1['award'] = JQ1.apply(lambda x: 1, axis=1)

dznames = ['DZ_authorID', 'assumeAwardYear', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt']
jqnames = ['JQ_affiliationID', 'JQ_sortedName', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt']
DZ2 = pd.read_csv(path11, sep='\t', header=None, names=dznames)
JQ2 = pd.read_csv(path22, sep='\t', header=None, names=jqnames)

DZ = pd.merge(DZ1, DZ2, on=['DZ_authorID'], how='inner')
DZnames = ['DZ_authorID', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']
DZ = DZ[DZnames]
dz_pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dz_" + '_'.join(DZnames) + ".txt"
DZ.to_csv(dz_pathOut, sep='\t', header=None, index=False)


JQ = pd.merge(JQ1, JQ2, on=['JQ_affiliationID', 'JQ_sortedName'])
JQnames = ['JQ_affiliationID', 'JQ_sortedName', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt', 'L', 'M', 'H', 'award']
JQ = JQ[JQnames]
jq_pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\jq_" + '_'.join(JQnames) + ".txt"
JQ.to_csv(jq_pathOut, sep='\t', header=None, index=False)
