# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
在PaperAuthorAffiliations.txt中找到
所有杰青发表的论文的paper id,以及下面的author id和affiliation id
"""
import pandas as pd
import csv
path1 = r"E:\FengXu\tmp\filtered_JQ_affiliationID_sortedName_fieldID_fieldName_" \
        r"paperID_authorID_paperYear_awardYear_citationCnt.txt"
path2 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
path3 = r"E:\FengXu\result1\jqPaperID_authorID_affID.txt"

bool_ = False

jq_paperIDs_set = set()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if bool_ is False:
            bool_ = True
            continue
        jq_paperIDs_set.add(line[4])

outer = open(path3, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in jq_paperIDs_set:
            outer.write(line[0]+'\t'+line[1]+'\t'+line[2]+'\n')
outer.close()
