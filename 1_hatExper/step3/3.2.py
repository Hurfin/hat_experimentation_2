# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
看看各领域还剩多少人
"""
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_" \
        r"bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_" \
        r"af_avejif_af_avecitation_af_avehindex_af_avepapercnt(buChuYi).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_" \
        r"bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_" \
        r"af_avejif_af_avecitation_af_avehindex_af_avepapercnt(chuYi).txt"

data1 = pd.read_csv(path1, sep='\t')

data1 = data1.groupby(['fieldID', 'fieldName']).size()
data1 = data1.reset_index()
data1.columns = ['fieldID', 'fieldName', 'authorCnt']
print(data1)
