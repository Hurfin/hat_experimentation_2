# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
"""
要找到co-author's first paper year

首先取得co-author的id
得到co-author的paper id
得到co-author的paper year
得到first paper year
"""
path1 = r'E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear(Co).txt'
names1 = ['paperID', 'authorID', 'affiliationID', 'paperYear']
data1 = pd.read_csv(path1, sep='\t', header=None, names=names1)
data1 = data1[['authorID']]
data1 = data1.drop_duplicates()

path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
names2 = ['paperID', 'authorID', 'affiliationID', 'authorSequenceNum']
data2 = pd.read_csv(path2, sep='\t', header=None, names=names2)
data2 = data2[['paperID', 'authorID']]

paperID_coAuthorID = data2.merge(data1, on=['authorID'], how='inner')
paperID_coAuthorID = paperID_coAuthorID[['paperID', 'authorID']]
del data1, data2
print('first step OK', "find co-author's all paper id")


path3 = r"D:\Dataset\NEW_MAG\Papers.txt"
papers = pd.read_csv(path3, sep='\t', header=None, usecols=[0, 7], names=['paperID', 'paperYear'])
papers = papers.dropna()
papers = papers.drop_duplicates()

paperID_coAuthorID_paperYear = paperID_coAuthorID.merge(papers, on=['paperID'], how='inner')
paperID_coAuthorID_paperYear = paperID_coAuthorID_paperYear[['paperID', 'authorID', 'paperYear']]
del papers, paperID_coAuthorID
print('second step OK', "find co-author's all paper year")

coAuthorID_firstPaperYear = paperID_coAuthorID_paperYear.groupby('authorID')['paperYear'].min()
coAuthorID_firstPaperYear = coAuthorID_firstPaperYear.reset_index()
coAuthorID_firstPaperYear.columns = ['authorID', 'firstPaperYear']
print('third step OK', "computed all co-author's first paper year")

paperID_authorID_affiliationID_paperYear = pd.read_csv(path1, sep='\t', header=None, names=names1)
paperID_authorID_affiliationID_paperYear_firstPaperYear = \
    paperID_authorID_affiliationID_paperYear.merge(
        coAuthorID_firstPaperYear,
        on=['authorID'],
        how='inner'
    )
paperID_authorID_affiliationID_paperYear_firstPaperYear = paperID_authorID_affiliationID_paperYear_firstPaperYear[
    ['paperID', 'authorID', 'affiliationID', 'paperYear', 'firstPaperYear']
]
print('merge finished')
pathOut = r"E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear_firstPaperYear(Co).txt"
paperID_authorID_affiliationID_paperYear_firstPaperYear.to_csv(pathOut, sep='\t', header=None, index=False)
