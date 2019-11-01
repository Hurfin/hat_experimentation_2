# -*- coding: utf-8 -*-
# !/usr/bin/env python
# (19820366, 'ping wang') (76130692, 'ping wang')
"""
上一步把有问题的杰青(19820366, 'ping wang') (76130692, 'ping wang')去除掉了

这里把co-author先合并(同authorID,同name为同一个人. 同affID, 同name为同一个人)在考虑用之前讨论的方式去筛选(即:
1. 找杰青们的first year的min和max，当作筛选条件1（上一个程序已经找过了）
min max为1980 2007
2016太晚了，发现对有些杰青，数据集里只有他获奖后的论文，获奖前没有论文，（要把这些杰青删掉）

2. 用 学术年龄>=10 作为条件筛选，学术年龄用co-author的 last paper year 减去 first paper year
对co-author用这个条件筛选的话，对杰青也应该这样筛选下（保留last paper year - first paper year >= 10的杰青，大概还剩929人）
)


本程序给被视为同一个人的学者加上了新的编号,fxID
"""
import pandas as pd
import csv
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\affID_" \
        r"sortedName_coAuthorID(drop_multi_CoAuthorID).txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['affID', 'sortedName', 'coAuthorID'])
print(data1.shape[0])
print(data1[['affID', 'sortedName']].drop_duplicates().shape[0])
print(data1[['coAuthorID']].drop_duplicates().shape[0])
data1 = data1.astype(str)

cnt = 1
index_ = str(cnt).zfill(6)
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\fxID_affID_sortedName_coAuthorID(drop_multi_CoAuthorID).txt"
index_record_dict = {}
with open(path_out, 'w', encoding='utf-8') as f:
    f.write('fxID\taffID\tsortedName\tcoAuthorID\n')
    for i in range(0, len(data1)):
        if data1.iloc[i]['coAuthorID'] in index_record_dict.keys():
            index_i = index_record_dict[data1.iloc[i]['coAuthorID']]  # 如果这个coAuthorID之前有了
            f.write(index_i+'\t'+data1.iloc[i]['affID']+'\t'+data1.iloc[i]['sortedName']+'\t'+
                    data1.iloc[i]['coAuthorID']+'\n')
        else:
            index_i = index_  # 获取fxID的编号
            index_record_dict[data1.iloc[i]['coAuthorID']] = index_i  # 记录这个coAuthorID对应的fxID编号
            f.write(index_i + '\t' + data1.iloc[i]['affID'] + '\t' + data1.iloc[i]['sortedName'] + '\t' +
                    data1.iloc[i]['coAuthorID'] + '\n')
            cnt += 1
            index_ = str(cnt).zfill(6)  # 用掉上一个编号后创建新编号
    pass
print(len(index_record_dict))