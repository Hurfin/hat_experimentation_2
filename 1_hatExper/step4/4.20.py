# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
r"E:\FengXu\tmp\filter_fxID_coAuthorID.txt"
r"E:\FengXu\result1\coAuthorPaperID_coAuthorPaperYear.txt"
r"E:\FengXu\result1\paperID_coAuthorID.txt"

这里得到
r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear.txt"
"""
import pandas as pd
import csv

path1 = r"E:\FengXu\tmp\filter_fxID_coAuthorID.txt"
path2 = r"E:\FengXu\result1\coAuthorID_coAuthorPaperID_coAuthorPaperYear.txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['fxID', 'coAuthorID'])
# coAuthorID	coAuthorPaperID	coAuthorPaperYear
data2 = pd.read_csv(path2, sep='\t')

data = pd.merge(data1, data2, on=['coAuthorID'], how='inner')
del data1, data2

data = data[['fxID', 'coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear']]

path_out1 = r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear.txt"
data.to_csv(path_out1, sep='\t', index=False)
