# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path = r"E:\FengXu\result\JIF\Papers_journal.txt"
path1 = r"E:\FengXu\result\JIF\Papers_journal_(has_journalID).txt"

colName = ['paperID', 'rank', 'doi', 'docType', 'paperTitle', 'originalTitle', 'bookTitle', 'year', 'date', 'publisher',
           'journalID', 'conferenceSeriesID', 'conferenceInstanceID', 'volume', 'issue', 'firstPage', 'lastPage',
           'referenceCount', 'citationCount', 'estimatedCitation']
data = pd.read_csv(path, sep='\t', header=None, names=colName)

data = data[data['journalID'] is not None and data['journalID'] != '']

data.to_csv(path1, sep='\t', header=None, index=False)
