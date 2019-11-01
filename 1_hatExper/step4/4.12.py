# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
由于coAuthor太多,这里对它们进行下筛选
1. 找杰青们的first year的min和max，当作筛选条件1（上一个程序已经找过了）
min max为1980 2007
2016太晚了，发现对有些杰青，数据集里只有他获奖后的论文，获奖前没有论文，（要把这些杰青删掉）

2. 用 学术年龄>=10 作为条件筛选，学术年龄用co-author的 last paper year 减去 first paper year
对co-author用这个条件筛选的话，对杰青也应该这样筛选下（保留last paper year - first paper year >= 10的杰青，大概还剩929人）


这里检查了一下coAuthor，发现只用affID和sortedName去标记一个人的话还不够，还要把affID不同、sortedName和coAuthorID相同的这些人，合并成同一个人

另外发现杰青里面有(19820366, 'ping wang') (76130692, 'ping wang') 这两个人，他俩authorID上有交集，但是手工查找后发现不是
同一个人，一个是浙大生物的，一个是中科院化学的。其它的杰青authorID都没有交集，明显错误，要把这两个人剔除掉

"""
import pandas as pd
import csv
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\affID_sortedName_coAuthorID(drop_multi_CoAuthorID).txt"
# path2 = r""

# data = pd.read_csv(path1, sep='\t', header=None, names=['affID', 'sortedName', 'coAuthorID'])
#
# print(data.shape[0])
# print(data.drop_duplicates().shape[0])
# print(data[['coAuthorID']].drop_duplicates().shape[0])

# data = data.groupby(['coAuthorID'])
# for coAuthorID, group in data:
#     if group.shape[0] > 1:
#         print(group)
#     pass


"""删除 这两个 wang ping"""
import os

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq\new_data\new_filter_jqRemain929.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq\new_data\splitByField" + '\\'
fieldNames = os.listdir(path2)

data1 = pd.read_csv(path1, sep='\t')
data1 = data1.astype(str)
with open(path1, 'w', encoding='utf-8') as f:
    f.write('affID\tsortedName\tawardYear\tfieldID\tfieldName\tminPaperYear\tmaxPaperYear\n')
    for i in range(0, len(data1)):
        if (data1.iloc[i]['affID'] == '19820366' and data1.iloc[i]['sortedName'] == 'ping wang') \
                or (data1.iloc[i]['affID'] == '76130692' and data1.iloc[i]['sortedName'] == 'ping wang'):
            continue
        # affID	sortedName	awardYear	fieldID	fieldName	minPaperYear	maxPaperYear
        sw = data1.iloc[i]['affID']+'\t'+data1.iloc[i]['sortedName']+'\t'+data1.iloc[i]['awardYear']+'\t'+ \
             data1.iloc[i]['fieldID']+'\t'+data1.iloc[i]['fieldName']+'\t'+data1.iloc[i]['minPaperYear']+'\t'+ \
             data1.iloc[i]['maxPaperYear']+'\n'
        f.write(sw)


for fieldName in fieldNames:
    path_i = path2 + fieldName
    data_i = pd.read_csv(path_i, sep='\t')
    data_i =  data_i.astype(str)
    with open(path_i, 'w', encoding='utf-8') as f:
        f.write('affID\tsortedName\tawardYear\tfieldID\tfieldName\tminPaperYear\tmaxPaperYear\n')
        for i in range(0, len(data_i)):
            if (data_i.iloc[i]['affID'] == '19820366' and data_i.iloc[i]['sortedName'] == 'ping wang') \
                    or (data_i.iloc[i]['affID'] == '76130692' and data_i.iloc[i]['sortedName'] == 'ping wang'):
                continue
            sw = data_i.iloc[i]['affID']+'\t'+data_i.iloc[i]['sortedName']+'\t'+data_i.iloc[i]['awardYear']+'\t'+\
                 data_i.iloc[i]['fieldID']+'\t'+data_i.iloc[i]['fieldName']+'\t'+data_i.iloc[i]['minPaperYear']+'\t'+\
                 data_i.iloc[i]['maxPaperYear']+'\n'
            f.write(sw)
    pass
