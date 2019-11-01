# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd
import numpy as np

path = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthorID_firstPaperYear" \
       r"(age5_25_CN_paperNum5more).txt"
names = ['coAuthorID', 'firstPaperYear']
data = pd.read_csv(path, sep='\t', header=None, names=names)

data = data.groupby('firstPaperYear')['coAuthorID'].count()
data = data.reset_index()
data.columns = ['firstPaperYear', 'authorCnt']
data = data.astype({'firstPaperYear': int})
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthor_firstPaperYear_authorCnt.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)
