# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as np
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\ans_JQ_map_coAuthor.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\2_affiliationID_authorEnglishNameSorted_" \
        r"minYear_awardYear_academicAge(academicAge5_25).txt"

data1 = pd.read_csv(path2, sep='\t', header=None, names=['affiliationID', 'sortedName', 'awardYear'], usecols=[0, 1, 3])

data2 = pd.read_csv(path1, sep='\t', header=None, names=['affiliationID', 'sortedName', 'compareAuthorID'])

data = data2.merge(data1, on=['affiliationID', 'sortedName'], how='inner')
data = data[['affiliationID', 'sortedName', 'compareAuthorID', 'awardYear']]
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(JQ_map_DZ)affiliationID"\
          r"_sortedName_compareAuthorID_assumeAwardYear.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)
