# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\field\affiliationID_sortedName_fatherFieldID.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\field\fields.txt"
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\field\affiliationID_sortedName_fatherFieldID_fieldName.txt"

names1 = ['affiliationID', 'sortedName', 'fatherFieldID']
data1 = pd.read_csv(path1, sep='\t', header=None, names=names1)
names2 = ['fatherFieldID', 'fieldName']
data2 = pd.read_csv(path2, sep='\t', header=None, names=names2)

data = pd.merge(data1, data2, on=['fatherFieldID'], how='inner')
del data1, data2
data = data[['affiliationID', 'sortedName', 'fatherFieldID', 'fieldName']]
data.to_csv(pathOut, sep='\t', header=None, index=False)
