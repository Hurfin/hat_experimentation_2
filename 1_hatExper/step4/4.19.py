# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
上一个程序筛选co-author，剩下16320个人
名单在文件
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\1\filter_" \
r"fxID_minYear_maxYear.txt"

r"E:\FengXu\result1\coAuthorPaperID_coAuthorPaperYear.txt"
r"E:\FengXu\result1\paperID_coAuthorID.txt"

得到r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\2\filter_" \
            r"fxID_coAuthorID.txt"
"""
import pandas as pd
import csv

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\1\filter_" \
        r"fxID_minYear_maxYear.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\1\fxID_" \
        r"affID_sortedName_coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt"

data1 = pd.read_csv(path1, sep='\t')
data2 = pd.read_csv(path2, sep='\t')

path_out1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\2\filter_" \
            r"fxID_coAuthorID.txt"

fxID_set = set()
bool_ = 1
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        if bool_ == 1:
            bool_ = 0
            continue
        line = line.strip('\n').split('\t')
        fxID_set.add(line[0])
    pass
bool_ = 1
with open(path_out1, 'w', encoding='utf-8') as f:
    with open(path2, 'r', encoding='utf-8') as ff:
        for line in ff:
            if bool_ == 1:
                bool_ = 0
                continue
            line = line.strip('\n').split('\t')
            if line[0] in fxID_set:
                f.write(line[0]+'\t'+line[3]+'\n')
        pass
    pass

