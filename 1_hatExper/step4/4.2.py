# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
开始找各个领域上杰青们的co-author

这里先把筛选整理后的杰青还跟之前一样，按领域分好
"""
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\filtered_JQ_affiliationID_sortedName_fieldID_fieldName_paperID_"\
        r"authorID_paperYear_awardYear_citationCnt.txt"

path2 = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\field_jq\\过滤后的新的各领域上的杰青\\"

data = pd.read_csv(path1, sep='\t')
data = data[['affID', 'sortedName', 'fieldID', 'fieldName']]
data = data.drop_duplicates()

data = data.groupby(['fieldID', 'fieldName'])

for key, group in data:
    path_construct = path2 + str(key[0]) + "_" + str(key[1]) + ".txt"
    group = group[['affID', 'sortedName']]
    group.to_csv(path_construct, sep='\t', index=False, header=None)
