# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np
path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\ans_JQ_map_coAuthor.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\DZ_authorID_assumeAwardYear_" \
           r"aveCitationCnt_aveJIF_aveH-Index_avePaperCnt(afterAward5Years).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_affiliationID_sortedName_" \
          r"aveCitationCnt_aveJIF_aveH-Index_avePaperCnt(afterAward5Years).txt"
data = pd.read_csv(path, sep='\t', header=None, names=['JQ_affiliationID', 'JQ_sortedName', 'DZ_authorID'])
data1 = pd.read_csv(path1, sep='\t', header=None,
                    names=['DZ_authorID', 'DZ_assumeAwardYear', 'DZ_aveCitationCnt',
                           'DZ_aveJIF', 'DZ_aveH-Index', 'DZ_avePaperCnt'])
data2 = pd.read_csv(path2, sep='\t', header=None,
                    names=['JQ_affiliationID', 'JQ_sortedName', 'JQ_aveCitationCnt',
                           'JQ_aveJIF', 'JQ_aveH-Index', 'JQ_avePaperCnt'])

data = data.merge(data1, on=['DZ_authorID'], how='inner')
data = data.merge(data2, on=['JQ_affiliationID', 'JQ_sortedName'], how='inner')
selectCols = [
    'DZ_authorID', 'DZ_assumeAwardYear', 'DZ_aveCitationCnt', 'DZ_aveJIF', 'DZ_aveH-Index', 'DZ_avePaperCnt',
    'JQ_affiliationID', 'JQ_sortedName', 'JQ_aveCitationCnt', 'JQ_aveJIF', 'JQ_aveH-Index', 'JQ_avePaperCnt'
]
data = data[selectCols]
print(len(data))

ansDF1 = data[['DZ_authorID', 'DZ_assumeAwardYear', 'DZ_aveCitationCnt', 'DZ_aveJIF', 'DZ_aveH-Index', 'DZ_avePaperCnt']]
ansDF2 = data[['JQ_affiliationID', 'JQ_sortedName', 'JQ_aveCitationCnt', 'JQ_aveJIF', 'JQ_aveH-Index', 'JQ_avePaperCnt']]
pathOut1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\DZ_authorID_" \
           r"DZ_assumeAwardYear_DZ_aveCitationCnt_DZ_aveJIF_DZ_aveH-Index_DZ_avePaperCnt(afterAward5Years).txt"
pathOut2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\JQ_affiliationID_" \
           r"JQ_sortedName_JQ_aveCitationCnt_JQ_aveJIF_JQ_aveH-Index_JQ_avePaperCnt(afterAward5Years).txt"

ansDF1.to_csv(pathOut1, sep='\t', header=None, index=False)
ansDF2.to_csv(pathOut2, sep='\t', header=None, index=False)
