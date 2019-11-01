# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"

fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear	journalID	minYear	maxYear
中的journalID列格式有问题"122181971.0"，去掉后面的零
"""
import pandas as pd
import csv

path1 = r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"
path2 = r""

data = []

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        l = list()
        for x in line:
            l.append(x)
        data.append(l)

flag = True
with open(path1, 'w', encoding='utf-8') as f:
    for i in range(0, len(data)):
        ll = data[i]
        ll[4] = ll[4].strip('.0')
        if flag is True:
            flag = False
            f.write('\t'.join(ll)+'\n')
            continue
        f.write('\t'.join(ll)+'\n')
