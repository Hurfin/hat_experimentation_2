# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
把筛选后的杰青的数据挑出来
以免后面处理时每次还得选出来这些人，比较麻烦

"""
import pandas as pd
import os

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_" \
        r"bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_" \
        r"af_avejif_af_avecitation_af_avehindex_af_avepapercnt(buChuYi).txt"
# path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_" \
#         r"bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_" \
#         r"af_avejif_af_avecitation_af_avehindex_af_avepapercnt(chuYi).txt"

path3 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_affiliationID_sortedName_fieldID_fieldName_paperID_" \
        r"authorID_paperYear_awardYear_citationCnt.txt"

data1 = pd.read_csv(path1, sep='\t')
data2 = pd.read_csv(path3, sep='\t', header=None,
                    names=['affID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID',
                           'paperYear', 'awardYear', 'citationCnt'])
data1 = data1[['affID', 'sortedName']]
data1 = data1.drop_duplicates()

data = pd.merge(data1, data2, on=['affID', 'sortedName'], how='inner')
pout = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\filtered_JQ_affiliationID_sortedName_fieldID_fieldName_paperID_" \
       r"authorID_paperYear_awardYear_citationCnt.txt"
data.to_csv(pout, sep='\t', index=False)
