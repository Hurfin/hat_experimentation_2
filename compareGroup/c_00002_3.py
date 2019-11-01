# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(JQ_map_DZ)" \
       r"affiliationID_sortedName_compareAuthorID_assumeAwardYear.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_" \
        r"paperYear_firstPaperYear(Co).txt"

data1 = pd.read_csv(path1, sep='\t', header=None,
                    names=['JQ_affiliationID', 'JQ_sortedName', 'DZ_authorID', 'DZ_assumeAwardYear'])
data2 = pd.read_csv(path2, sep='\t', header=None,
                    names=['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear', 'DZ_firstPaperYear'])
data = data2.merge(data1, on=['DZ_authorID'], how='inner')
selectCols = ['DZ_paperID', 'DZ_authorID', 'DZ_affiliationID', 'DZ_paperYear',
              'DZ_firstPaperYear', 'JQ_affiliationID', 'JQ_sortedName', 'DZ_assumeAwardYear']
data = data[selectCols]
pathOut = "E:/pythonCode/RJ_experimentation_1/Data/compareGroupData/coAuthor/selectedCoAuthor/"
pathOut = pathOut + "(DZ)" + '_'.join(selectCols) + ".txt"

data.to_csv(pathOut, sep='\t', header=None, index=False)
