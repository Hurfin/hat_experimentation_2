# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
path1 = r"E:\FengXu\result\JIF\JieqingContribute_JournalID.txt"
path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
path3 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
pathOut = r"E:\FengXu\result\JIF\journalID_JIF_perYear_from1989to2019.txt"
"""
import pandas as pd
path1 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"


paperID_referenceID = pd.read_csv(path1, sep='\t', header=None, names=['paperID1', 'referenceID1'])
paperID_year_journal = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'year'], usecols=[0, 1])

# yearList = list(range(1989, 2000))
yearList = list(range(2000, 2010))
# yearList = list(range(2010, 2020))

for year in yearList:
    paperID_thisYear = paperID_year_journal[paperID_year_journal['year'] == year]['paperID']
    paperIDThisYear_referenceID = paperID_referenceID.merge(
        paperID_thisYear, left_on='paperID1', right_on='paperID', how='inner')
    paperIDThisYear_referenceID = paperIDThisYear_referenceID[['paperID1', 'referenceID1']]
    referenceID_citationCntThisYear = paperIDThisYear_referenceID.groupby('referenceID1').count()
    referenceID_citationCntThisYear = referenceID_citationCntThisYear.reset_index()
    referenceID_citationCntThisYear.columns = ['referenceID', 'citationCnt']

    pathOut = r"E:\FengXu\result\JIF\referenceID_citationCnt_perYear\referenceID_citationCnt({}).txt".format(year)
    referenceID_citationCntThisYear.to_csv(pathOut, sep='\t', header=None, index=False)
    pass
