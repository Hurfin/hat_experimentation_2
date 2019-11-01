# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\ans_compare_coAuthorID.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID_" \
        r"paperYear_firstPaperYear(Co).txt"

data1 = pd.read_csv(path1, sep='\t', header=None, names=['authorID'])
data2 = pd.read_csv(path2, sep='\t', header=None,
                    names=['paperID', 'authorID', 'affiliationID', 'paperYear', 'firstPaperYear'])
data = data2.merge(data1, on=['authorID'], how='inner')
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\(compareGroup)" \
          r"paperID_affiliationID_" \
          r"paperYear_firstPaperYear.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)
