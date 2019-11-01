# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path1 = r"E:\FengXu\result\TMP\paperID_authorID_affiliationID_paperYear_firstPaperYear(Co).txt"
path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
path3 = r"D:\Dataset\NEW_MAG\Papers.txt"
data1 = pd.read_csv(path1, sep='\t', header=None,
                    names=['paperID', 'authorID', 'affiliationID', 'paperYear', 'firstPaperYear'])

data1 = data1[['authorID']]
data1 = data1.drop_duplicates()

data2 = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'authorID', 'affiliationID', 'authorSequenceNum'])

data2 = data2[['paperID', 'authorID']]

data = pd.merge(data1, data2, on=['authorID'], how='inner')
data = data[['paperID', 'authorID']]
del data1, data2
data = data.drop_duplicates()
print('table1 len=', data.shape[0])

data3 = pd.read_csv(path3, sep='\t', usecols=[0, 7], names=['paperID', 'paperYear'])
data3 = data3.dropna()
data3 = data3[(data3['paperYear'] >= 1989)]
data3 = data.drop_duplicates()
print('table2 len=', data3.shape[0])

data = pd.merge(data, data3, on=['paperID'], how='inner')
del data3
data = data[['paperID', 'authorID', 'paperYear']]

data.to_csv(r"E:\FengXu\result\TMP\paperID_authorID_paperYear(coPaperALL).txt", sep='\t', header=None, index=False)
