# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
path1 = r"E:\FengXu\result\compareGroupData\Jieqing_paperID_year"
path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
pathOut = r"E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear(JQ_Co).txt"
names1 = ['paperID', 'paperYear']
names2 = ['paperID', 'authorID', 'affiliationID', 'authorSequenceNum']
data1 = pd.read_csv(path1, sep='\t', header=None, names=names1)
data2 = pd.read_csv(path2, sep='\t', header=None, names=names2)
data = data1.merge(data2, on=['paperID'], how='inner')
del data1, data2
data = data[['paperID', 'authorID', 'affiliationID', 'paperYear']]
data = data.drop_duplicates()
data.to_csv(pathOut, sep='\t', header=None, index=False)