# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path1 = r"D:\Dataset\NEW_MAG\Authors.txt"
authorID_authorNormalizedName_authorDisplayName = pd.read_csv(path1, sep='\t', header=None, usecols=[0, 2, 3])
authorID_authorNormalizedName_authorDisplayName.columns = ['authorID', 'normalizedName', 'displayName']
authorID_authorNormalizedName_authorDisplayName = authorID_authorNormalizedName_authorDisplayName.drop_duplicates()

path2 = r"E:\FengXu\result\JieqingContain_paperID_authorID_affiliationID_paperYear"
JieqingContain_paperID_authorID_affiliationID_paperYear = pd.read_csv(path2, sep='\t', header=None)
JieqingContain_paperID_authorID_affiliationID_paperYear.columns = ['paperID', 'authorID', 'affiliationID', 'paperYear']

JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName = \
    JieqingContain_paperID_authorID_affiliationID_paperYear.merge(
        authorID_authorNormalizedName_authorDisplayName,
        on=['authorID'],
        how='inner'
    )

JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName = \
    JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName[
        ['paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'displayName']
    ]
JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.to_csv(
    r"E:\FengXu\result\JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.txt",
    sep='\t',
    header=None,
    index=False
)
