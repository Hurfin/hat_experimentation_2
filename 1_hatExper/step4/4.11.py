# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已经有了
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\affID_sortedName_coAuthorID(drop_multi_CoAuthorID).txt"

但coAuthor太多下一步对它们进行下筛选
1. 找杰青们的first year的min和max，当作筛选条件1
min max为1980 2016(jq筛选后为1980 2007)
2016太晚了，发现对有些杰青，数据集里只有他获奖后的论文，获奖前没有论文，（要把这些杰青删掉）

2. 用 学术年龄>=10 作为条件筛选，学术年龄用co-author的last paper year 减去 first paper year
对co-author用这个条件筛选的话，对杰青也应该这样筛选下（保留last paper year - first paper year >= 10的杰青，大概还剩929人）

现在只对杰青进行了筛选，处理后新的杰青的名单在
E:\\pythonCode\\RJ_experimentation_1\\Data_1\\field_jq\\new_data
路径下

下一步对co-author进行处理
"""
import pandas as pd
import csv

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\filtered_" \
        r"JQ_affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"

# affID	sortedName	fieldID	fieldName	paperID	authorID	paperYear	awardYear	citationCnt
data1 = pd.read_csv(path1, sep='\t')

data1 = data1[['affID', 'sortedName', 'paperYear', 'awardYear', 'fieldID', 'fieldName']]
data1 = data1.astype({'affID': str, 'sortedName': str, 'paperYear': int, 'awardYear': int, 'fieldID': str, 'fieldName': str})

data11 = data1.groupby(['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName'])['paperYear'].min()
data11 = data11.reset_index()
data11.columns = ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName', 'minPaperYear']

data22 = data1.groupby(['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName'])['paperYear'].max()
data22 = data22.reset_index()
data22.columns = ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName', 'maxPaperYear']

data = pd.merge(data11, data22, on=['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName'], how='inner')
data = data[['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName', 'minPaperYear', 'maxPaperYear']]

# print(min(list(data11['minPaperYear'])), max(list(data11['minPaperYear'])))  # 1980 2016
# # print(data1.loc[data1['minPaperYear'] >= 2010])
# print(data11.loc[data1.minPaperYear > data11.awardYear])
# print(data11.loc[data1.minPaperYear > data11.awardYear].shape)

# 2582107416	2639210271	19820366	4
# 2492898075	2639210271	19820366	3

print(data.shape[0])
print(data[data['minPaperYear'] < data['awardYear']].shape[0])
data = data[data['minPaperYear'] < data['awardYear']]  # 把firstPaperYear在awardYear之后的删除掉
print(data[data['maxPaperYear']-data['minPaperYear'] >= 10].shape[0])
data = data[data['maxPaperYear']-data['minPaperYear'] >= 10]

# ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName', 'minPaperYear', 'maxPaperYear']
print(data.groupby(['fieldID', 'fieldName']).size())

path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq\new_data\new_filter_jqRemain929.txt"
data.to_csv(path_out, sep='\t', index=False)

# jq筛选后的minPaperYear的min和max
print(min(list(data['minPaperYear'])), max(list(data['minPaperYear'])))

path_out_ = "E:\\pythonCode\\RJ_experimentation_1\\Data_1\\field_jq\\new_data\\splitByField\\"
data = data.groupby(['fieldID', 'fieldName'])
for fID_fNAME, group in data:
    path_i = path_out_ + fID_fNAME[0] + '_' + fID_fNAME[1] + '.txt'
    group.to_csv(path_i, index=False, sep='\t')
    pass


