# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
续上，将找到的paper year和之前的引用关系合并得到paper id、reference id、paper year
至此得到一个有用的、用来算aveCitation的数据
"""
import pandas as pd

path_year = r"E:\FengXu\tmp\paperID_paperYear.txt"
path_ref = r"E:\FengXu\result1\paperReferences(refJQ).txt"

data1 = pd.read_csv(path_year, sep='\t', header=None, names=['paperID', 'paperYear'])
data2 = pd.read_csv(path_ref, sep='\t', header=None, names=['paperID', 'refID'])

data1 = data1.drop_duplicates()
data2 = data2.drop_duplicates()

data = pd.merge(data1, data2, on=['paperID'], how='inner')
del data1, data2
data = data[['paperID', 'refID', 'paperYear']]
path_out = r"E:\FengXu\result1\paperID_refID_paperYear(refJQ).txt"
data.to_csv(path_out, sep='\t', header=None, index=False)
