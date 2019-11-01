# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
# 上一个程序把co-author合并了(同authorID,同name为同一个人. 同affID, 同name为同一个人)
#
# 现在考虑用之前讨论的方式去筛选(即:
# 1. 找杰青们的first year的min和max，当作筛选条件1（上一个程序已经找过了）
# min max为1980 2007
# 2016太晚了，发现对有些杰青，数据集里只有他获奖后的论文，获奖前没有论文，（要把这些杰青删掉）
#
# 2. 用 学术年龄>=10 作为条件筛选，学术年龄用co-author的 last paper year 减去 first paper year
# 对co-author用这个条件筛选的话，对杰青也应该这样筛选下（保留last paper year - first paper year >= 10的杰青，大概还剩929人）
# )
#
# 这里先找 co-author 的 first paper year 和 last paper year

上一步找到了r"E:\FengXu\result1\coAuthorPaperID_coAuthorPaperYear.txt"

续上,继续找,得到了r"E:\FengXu\result1\coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt"

"""
import pandas as pd
import csv

path1 = r"E:\FengXu\result1\coAuthorPaperID_coAuthorPaperYear.txt"
path2 = r"E:\FengXu\result1\paperID_coAuthorID.txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['coAuthorPaperID', 'coAuthorPaperYear'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'coAuthorID'])

data = pd.merge(data1, data2, left_on=['coAuthorPaperID'], right_on=['paperID'], how='inner')
del data1, data2

data = data[['coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear']]

path_out1 = r"E:\FengXu\result1\coAuthorID_coAuthorPaperID_coAuthorPaperYear.txt"
data.to_csv(path_out1, sep='\t', index=False)
data = data.astype({'coAuthorID': str, 'coAuthorPaperID': str, 'coAuthorPaperYear': int})

path_out2 = r"E:\FengXu\result1\coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt"
outer1 = open(path_out2, 'w', encoding='utf-8')
data = data.groupby(['coAuthorID'])
for coAuthorID, group in data:
    minYear = min(list(group['coAuthorPaperYear']))
    maxYear = max(list(group['coAuthorPaperYear']))
    outer1.write(coAuthorID+'\t'+str(minYear)+'\t'+str(maxYear)+'\n')
    pass
outer1.close()
