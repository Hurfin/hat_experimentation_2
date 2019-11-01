# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
去掉2012以后获奖的杰青（原因是最新的数据不全面）

"""
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_" \
           r"aveJIF_aveCitation_aveHindex_avePaperCnt(before_after5_citationBuChuYiLunWenShu).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\affID_sortedName_fieldID_fieldName_" \
           r"aveJIF_aveCitation_aveHindex_avePaperCnt(before_after5_citationChuYiLunWenShu).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_affiliationID_sortedName_fieldID_fieldName_" \
        r"paperID_authorID_paperYear_awardYear_citationCnt.txt"

names1 = ['affID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID', 'paperYear', 'awardYear', 'citationCnt']
data1 = pd.read_csv(path3, sep='\t', header=None, names=names1)
data1 = data1[['affID', 'sortedName', 'awardYear']]
data1 = data1[data1['awardYear'] <= 2012]
data1 = data1.drop_duplicates()

# affID	sortedName	fieldID	fieldName	bf_avejif	bf_avecitation	bf_avehindex
# bf_avepapercnt	af_avejif	af_avecitation	af_avehindex	af_avepapercnt
data2 = pd.read_csv(path1, sep='\t')  # 不除以
data = pd.merge(data1, data2, on=['affID', 'sortedName'], how='inner')
data = data[['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName',
             'bf_avejif', 'bf_avecitation', 'bf_avehindex', 'bf_avepapercnt',
             'af_avejif', 'af_avecitation', 'af_avehindex', 'af_avepapercnt']]
path_out1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1" + "\\" + '_'.join(
            ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName',
             'bf_avejif', 'bf_avecitation', 'bf_avehindex', 'bf_avepapercnt',
             'af_avejif', 'af_avecitation', 'af_avehindex', 'af_avepapercnt']) + "(buChuYi).txt"
data.to_csv(path_out1, sep='\t', index=False)

data3 = pd.read_csv(path2, sep='\t')  # 除以
data = pd.merge(data1, data3, on=['affID', 'sortedName'], how='inner')
data = data[['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName',
             'bf_avejif', 'bf_avecitation', 'bf_avehindex', 'bf_avepapercnt',
             'af_avejif', 'af_avecitation', 'af_avehindex', 'af_avepapercnt']]
path_out2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1" + "\\" + '_'.join(
            ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName',
             'bf_avejif', 'bf_avecitation', 'bf_avehindex', 'bf_avepapercnt',
             'af_avejif', 'af_avecitation', 'af_avehindex', 'af_avepapercnt']) + "(chuYi).txt"
data.to_csv(path_out2, sep='\t', index=False)
