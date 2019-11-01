# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
用
r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq\new_data\new_filter_jqRemain929.txt"
来筛选下面的数据
r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\affID_sortedName_fxID_dist.txt"

保存为
r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\filtered_affID_sortedName_fxID_dist.txt"
"""
import pandas as pd
# affID	sortedName	awardYear	fieldID	fieldName	minPaperYear	maxPaperYear
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq\new_data\new_filter_jqRemain929.txt"
#
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\affID_sortedName_fxID_dist.txt"

data1 = pd.read_csv(path1, sep='\t')
data2 = pd.read_csv(path2, sep='\t', header=None, names=['affID', 'sortedName', 'fxID', 'dist'])

data1 = data1[['affID', 'sortedName']]

data = pd.merge(data1, data2, on=['affID', 'sortedName'], how='inner')
del data1, data2
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\filtered_" \
           r"affID_sortedName_fxID_dist.txt"
data = data[['affID', 'sortedName', 'fxID', 'dist']]
data.to_csv(path_out, sep='\t', index=False)
