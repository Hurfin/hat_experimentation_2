# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd

path1 = r"E:\FengXu\result\compareGroupData\tmp\Jieqing_paperIDs.txt"

jieqing_paperID = pd.read_csv(path1, sep='\t', header=None, names=['paperID'])


path2 = r"D:\Dataset\NEW_MAG\Papers.txt"
ucols = [0, 7]
papers = pd.read_csv(path2, sep='\t', header=None, usecols=ucols, names=['paperID', 'paperYear'])
papers = papers.drop_duplicates()

pathOut = r"E:\FengXu\result\compareGroupData\Jieqing_paperID_year"

papers = papers.merge(jieqing_paperID, on=['paperID'], how='inner')
papers = papers[['paperID', 'paperYear']]
papers.to_csv(pathOut, sep='\t', header=None, index=False)
