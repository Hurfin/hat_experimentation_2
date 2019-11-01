# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np
path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
       r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_awardYear_" \
       r"citationCnt.txt"
pathOut = r"C:\Users\12433\Desktop\tmp_data\jq_paperIDs.txt"
set_ = set()
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        set_.add(line[0])
    pass

l = list(set_)

with open(pathOut, 'w', encoding='utf-8') as f:
    for pid in l:
        f.write(pid+'\n')
