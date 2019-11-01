# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd
path = r"D:\Dataset\NEW_MAG\Papers.txt"
pathOut = r"E:\FengXu\result\JIF\Papers_journal.txt"
colName = ['paperID', 'rank', 'doi', 'docType', 'paperTitle', 'originalTitle', 'bookTitle', 'year', 'date', 'publisher',
           'journalID', 'conferenceSeriesID', 'conferenceInstanceID', 'volume', 'issue', 'firstPage', 'lastPage',
           'referenceCount', 'citationCount', 'estimatedCitation']
papers = pd.read_csv(path, sep='\t', header=None, names=colName)

papers = papers[papers['docType'] == 'Journal']
papers.to_csv(pathOut, sep='\t', header=None, index=False)
