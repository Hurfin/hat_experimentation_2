# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
开始找各个领域上杰青们的co-author

把筛选整理后的杰青的所有与论文相关的数据按领域分开存放

"""
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\filtered_JQ_affiliationID_sortedName_fieldID_fieldName_paperID_" \
       r"authorID_paperYear_awardYear_citationCnt.txt"

path2 = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\field_jq\\过滤后的新的各领域上的杰青的所有数据\\"

data = pd.read_csv(path1, sep='\t')

data = data.groupby(['fieldID', 'fieldName'])

for key, group in data:
    path_construct = path2 + "paperData_" + str(key[0]) + "_" + str(key[1]) + ".txt"
    group.to_csv(path_construct, sep='\t', index=False)

