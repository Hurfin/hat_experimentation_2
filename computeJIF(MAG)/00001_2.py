# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd
path = r"E:\FengXu\result\JIF\JieqingContribute_paperID_year_JournalID.txt"
pathOut = r"E:\FengXu\result\JIF\JieqingContribute_JournalID.txt"
data = pd.read_csv(path, sep='\t', header=None, usecols=[2])
data.columns = ['journalID']
data = data.drop_duplicates()
data.to_csv(pathOut, sep='\t', header=None, index=False)
