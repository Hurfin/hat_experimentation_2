# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已经有了
E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\合作者的id和sortedName\coAuthorID_sortedName.txt
在
    r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\杰青论文id下的所有作者" \
    r"以及机构数据\filterCN_jqPaperID_authorID_affID.txt"
中把对应的affID找到
"""
import pandas as pd
import csv

path1 = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\co-authorData\\coAuthorID_sortedName.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\filterCN_" \
        r"jqPaperID_authorID_affID.txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['coAuthorID', 'sortedName'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=['jqPaperID', 'authorID', 'affID'])

data1 = data1.drop_duplicates()
data2 = data2.drop_duplicates()

data = pd.merge(data1, data2, left_on=['coAuthorID'], right_on=['authorID'], how='inner')
del data1, data2
data = data[['coAuthorID', 'affID', 'sortedName']]
data = data.drop_duplicates()

path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_" \
           r"sortedName)\coAuthorID_affID_sortedName.txt"
data.to_csv(path_out, sep='\t', header=None, index=False)
print(data.shape[0])
print(len(data.groupby(['affID', 'sortedName'])))

