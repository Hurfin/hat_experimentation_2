# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as no
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\citaitonData\paperID_citationCnt(DZ).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(DZ)" \
        r"DZ_paperID_DZ_authorID_DZ_affiliationID_DZ_paperYear_DZ_firstPaperYear_JQ_affiliationID_" \
        r"JQ_sortedName_DZ_assumeAwardYear.txt"
names = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
         'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName', 'DZ_assumeAwardYear']
data1 = pd.read_csv(path2, sep='\t', header=None, names=names)
data2 = pd.read_csv(path1, sep='\t', header=None, names=['DZ_paperID', 'DZ_citationCnt'])

data = pd.merge(data1, data2, on=['DZ_paperID'], how='left')
selectCols = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
              'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName', 'DZ_assumeAwardYear', 'DZ_citationCnt']
data = data[selectCols]
data = data.fillna(0)
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(DZ)" \
          r"DZ_paperID_DZ_authorID_DZ_affiliationID_DZ_paperYear_DZ_firstPaperYear_JQ_affiliationID_" \
          r"JQ_sortedName_DZ_assumeAwardYear_DZ_citationCnt.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)