# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
根据统计出的杰青的affiliation id，对paperAuthorAffiliation.txt进行过滤
"""
import pandas as pd

path1 = "E:/FengXu/Data/name_affID.txt"
JieQing_name_affID = pd.read_csv(path1, sep='\t', header=None)
JieQing_name_affID.columns = ['name', 'affiliationID']
JieQing_afID = JieQing_name_affID[['affiliationID']]
del JieQing_name_affID
JieQing_afID = JieQing_afID.drop_duplicates()


path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
paperAuthorAffiliation = pd.read_csv(path2, header=None, sep='\t')
paperAuthorAffiliation.columns = ['paperID', 'authorID', 'affiliationID', 'authorSequenceNumber']
paperID_authorID_affiliationID = paperAuthorAffiliation[['paperID', 'authorID', 'affiliationID']]

filterJieqing_paperID_authorID_affiliationID = paperID_authorID_affiliationID.merge(JieQing_afID, on=['affiliationID'], how='inner')

filterJieqing_paperID_authorID_affiliationID.to_csv("filterJieqing_paperID_authorID_affiliationID.txt", sep='\t', header=None, index=False)
