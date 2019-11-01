# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path = r"E:\FengXu\result\JIF\Papers_journal.txt"
path1 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
colName = ['paperID', 'rank', 'doi', 'docType', 'paperTitle', 'originalTitle', 'bookTitle', 'year', 'date', 'publisher',
           'journalID', 'conferenceSeriesID', 'conferenceInstanceID', 'volume', 'issue', 'firstPage', 'lastPage',
           'referenceCount', 'citationCount', 'estimatedCitation']
data = pd.read_csv(path, header=None, sep='\t', names=colName)
data = data[['paperID', 'year', 'journalID']]
data = data.dropna()
data.to_csv(path1, sep='\t', header=None, index=False)
