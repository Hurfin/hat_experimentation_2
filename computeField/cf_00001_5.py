# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\author\unique.txt"

path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_" \
        r"affiliationID_sortedName_aveCitationCnt_aveJIF_aveH-Index_avePaperCnt(afterAward5Years).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_" \
        r"affiliationID_sortedName_aveCitationCnt_aveJIF_aveH-Index_avePaperCnt(beforeAward5Years).txt"

path4 = r"E:\pythonCode\RJ_experimentation_1\Data\field\affiliationID_sortedName_fatherFieldID_fieldName.txt"

pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\field\fieldID_fieldName_aveCitationCnt(before_after)_" \
          r"aveJIF(before_after)_aveHIndex(before_after)_avePaperCnt(before_after).txt"


data1 = pd.read_csv(path1, sep='\t', header=None, names=['affiliationID', 'sortedName'])
data2 = pd.read_csv(path4, sep='\t', header=None, names=['affiliationID', 'sortedName', 'fatherFieldID', 'fieldName'])
data11 = pd.merge(data1, data2, on=['affiliationID', 'sortedName'], how='inner')
del data1, data2
data11 = data11[['affiliationID', 'sortedName', 'fatherFieldID', 'fieldName']]

data3 = pd.read_csv(path2, sep='\t', header=None,
                    names=['affiliationID', 'sortedName', 'after5_aveCitationCnt', 'after5_aveJIF',
                           'after5_aveHIndex', 'after5_avePaperCnt'])
data4 = pd.read_csv(path3, sep='\t', header=None,
                    names=['affiliationID', 'sortedName', 'before5_aveCitationCnt', 'before5_aveJIF',
                           'before5_aveHIndex', 'before5_avePaperCnt'])


data11 = pd.merge(data11, data3, on=['affiliationID', 'sortedName'], how='inner')
data11 = data11[['affiliationID', 'sortedName', 'fatherFieldID', 'fieldName', 'after5_aveCitationCnt', 'after5_aveJIF',
                 'after5_aveHIndex', 'after5_avePaperCnt']]
data11 = pd.merge(data11, data4, on=['affiliationID', 'sortedName'], how='inner')
data11 = data11[['affiliationID', 'sortedName', 'fatherFieldID', 'fieldName', 'after5_aveCitationCnt', 'after5_aveJIF',
                 'after5_aveHIndex', 'after5_avePaperCnt', 'before5_aveCitationCnt', 'before5_aveJIF',
                 'before5_aveHIndex', 'before5_avePaperCnt']]
del data3, data4
fout = open(pathOut, 'w', encoding='utf-8')

data11 = data11.groupby(['fatherFieldID', 'fieldName'])
for ffID_fName, group in data11:
    gp_len = group.shape[0]  # 该领域人数

    before5_aveCitationCnt_sum = group['before5_aveCitationCnt'].sum()/gp_len
    after5_aveCitationCnt_sum = group['after5_aveCitationCnt'].sum()/gp_len

    before5_aveJIF_sum = group['before5_aveJIF'].sum()/gp_len
    after5_aveJIF_sum = group['after5_aveJIF'].sum()/gp_len

    before5_aveHIndex_sum = group['before5_aveHIndex'].sum()/gp_len
    after5_aveHIndex_sum = group['after5_aveHIndex'].sum()/gp_len

    before5_avePaperCnt_sum = group['before5_avePaperCnt'].sum()/gp_len
    after5_avePaperCnt_sum = group['after5_avePaperCnt'].sum()/gp_len

    fout.write(str(ffID_fName[0])+'\t'+str(ffID_fName[1])+'\t'+
               str(before5_aveCitationCnt_sum)+'\t'+str(after5_aveCitationCnt_sum)+'\t'+
               str(before5_aveJIF_sum)+'\t'+str(after5_aveJIF_sum)+'\t'+
               str(before5_aveHIndex_sum)+'\t'+str(after5_aveHIndex_sum)+'\t'+
               str(before5_avePaperCnt_sum)+'\t'+str(after5_avePaperCnt_sum)+'\n')
    pass
fout.close()
