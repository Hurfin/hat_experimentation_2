# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd

path = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_" \
       r"affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
names2 = ['affID', 'sortedName', 'fieldID', 'fieldName', 'paperID', 'authorID', 'paperYear', 'awardYear', 'citationCnt']

data = pd.read_csv(path, sep='\t', header=None, names=names2)
print(data.dtypes)
data.astype()