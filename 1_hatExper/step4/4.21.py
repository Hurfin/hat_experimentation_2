# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已有
r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear.txt"

得到
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_minYear_maxYear.txt"

"""
import pandas as pd
import csv

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\1\filter_fxID_minYear_maxYear.txt"

# fxID	coAuthorID	coAuthorPaperID	coAuthorPaperYear
data1 = pd.read_csv(path1, sep='\t')
# fxID	minYear	maxYear
data2 = pd.read_csv(path2, sep='\t')

print(data1.shape[0], data2.shape[0])
data = pd.merge(data1, data2, on=['fxID'], how='inner')
del data1, data2

data = data[['fxID', 'coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear', 'minYear', 'maxYear']]
print(data.shape[0])

path_out1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
            r"(affID_sortedName)\3\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_minYear_maxYear.txt"
data.to_csv(path_out1, sep='\t', index=False)
