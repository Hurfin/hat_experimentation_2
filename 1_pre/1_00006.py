# -*- coding: utf-8 -*-
# !/usr/bin/env python

import pandas as pd

path = r"E:\FengXu\result\filterJieqing_paperID_authorID_affiliationID.txt"
Jieqing_paperID_authorID_affiliationID = pd.read_csv(path, sep='\t', header=None)
Jieqing_paperID_authorID_affiliationID.columns = ['paperID', 'authorID', 'affiliationID']

JieqingContain_paperID = Jieqing_paperID_authorID_affiliationID[['paperID']]
JieqingContain_paperID = JieqingContain_paperID.drop_duplicates()

path1 = r"D:\Dataset\NEW_MAG\Papers.txt"
paperID_paperYear = pd.read_csv(path1, sep='\t', header=None, usecols=[0, 7])
paperID_paperYear.columns = ['paperID', 'paperYear']
paperID_paperYear = paperID_paperYear.drop_duplicates()

JieqingContain_paperID_paperYear = paperID_paperYear.merge(JieqingContain_paperID, on=['paperID'], how='inner')


JieqingContain_paperID_authorID_affiliationID_paperYear = Jieqing_paperID_authorID_affiliationID.merge(
    JieqingContain_paperID_paperYear,
    left_on=['paperID'],
    right_on=['paperID'],
    how='inner'
)
JieqingContain_paperID_authorID_affiliationID_paperYear = JieqingContain_paperID_authorID_affiliationID_paperYear[
    ['paperID', 'authorID', 'affiliationID', 'paperYear']
]
JieqingContain_paperID_authorID_affiliationID_paperYear.to_csv(
    r"E:\FengXu\result\JieqingContain_paperID_authorID_affiliationID_paperYear", sep="\t", header=None, index=False
)

