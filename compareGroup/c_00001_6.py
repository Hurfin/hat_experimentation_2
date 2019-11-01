# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthor_age5_25_Aff_CN_paperNum5more.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_" \
        r"paperYear_firstPaperYear(Co).txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['authorID'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=['authorID', 'firstPaperYear'], usecols=[1, 4])

data1 = data1.drop_duplicates()
data2 = data2.drop_duplicates()

data = data1.merge(data2, on=['authorID'], how='inner')
data = data[['authorID', 'firstPaperYear']]
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthorID_firstPaperYear" \
          r"(age5_25_CN_paperNum5more).txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)
