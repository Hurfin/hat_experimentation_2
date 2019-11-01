# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
筛选引用文件为期刊paper的相互引用
"""
import pandas as pd

path1 = r"D:\Dataset\NEW_MAG\PaperReferences.txt"
path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
path3 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
colnames1 = ['paperID1', 'referenceID1']
colnames2 = ['paperID', 'year', 'journalID']
data1 = pd.read_csv(path1, sep='\t', header=None, names=colnames1)
data2 = pd.read_csv(path2, sep='\t', header=None, names=colnames2)
data2 = data2[['paperID']]
data2 = data2.drop_duplicates()

data = data1.merge(data2, left_on='paperID1', right_on='paperID', how='inner')
data = data.drop('paperID', axis=1)
data = data.merge(data2, left_on='referenceID1', right_on='paperID', how='inner')
data = data.drop('paperID', axis=1)

data.to_csv(path3, sep='\t', header=None, index=False)
