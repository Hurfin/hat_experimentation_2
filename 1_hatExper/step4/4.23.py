# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""

"""
import pandas as pd
import csv

path1 = r"E:\FengXu\result1\coAuthorPaperID_journalID.txt"
path2 = r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_minYear_maxYear.txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['coAuthorPaperID', 'journalID'])
# fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear	minYear	maxYear
data2 = pd.read_csv(path2, sep='\t')

data = pd.merge(data2, data1, on=['coAuthorPaperID'], how='left')
data = data[['fxID', 'coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear', 'journalID', 'minYear', 'maxYear']]

data['journalID'] = data['journalID'].fillna('#')
# print(data[data['journalID'] == '#'].shape[0])
# print(data.shape[0])
# for i in range(data.shape[0]):
#     journalID_i = data.iloc[i]['journalID']
#     if journalID_i != '#':
#         journalID_i = journalID_i.rstrip('.0')
#         data.iloc[i]['journalID'] = journalID_i
#     pass

path_out1 = r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"
data.to_csv(path_out1, sep='\t', index=False)

