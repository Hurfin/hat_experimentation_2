# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd

path = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
path1 = r"E:\FengXu\result\JIF\1_paperID_year_journalID(papersJournal).txt"
ColName = ['paperID', 'year', 'journalID']
data = pd.read_csv(path, sep='\t', header=None, names=ColName)
data = data.drop_duplicates()
data.to_csv(path1, sep='\t', header=None, index=False)
