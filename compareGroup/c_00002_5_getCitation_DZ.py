# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as np
import pandas as pd
path1 = r"D:\Dataset\NEW_MAG\PaperReferences.txt"
path2 = r"E:\FengXu\result\HPData\DZ_paperID.txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['paperID', 'referenceID'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=['paperID_DZ'])
data1 = data1.merge(data2, left_on='referenceID', right_on='paperID_DZ', how='inner')
data1 = data1[['paperID', 'referenceID']]
data1 = data1.groupby('referenceID')['paperID'].count()
data1 = data1.reset_index()
data1.columns = ['referenceID', 'citationCnt']
pathOut = r'E:\FengXu\result\paperID_citationCnt(DZ).txt'
data1.to_csv(pathOut, sep='\t', header=None, index=False)
