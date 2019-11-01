# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
author id, affiliation id, paper year,
"""
DICT_authorID_minYear_awardYear = {}  # author id的最早发论文的年份
# path1 = r"E:\FengXu\result\JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"

# 只保留一个作者(name, affiliation id相同的视为同一个人)最早发的论文的信息
FULL_doc = []
with open(path1, "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        FULL_doc.append(line)
        if line[1] not in DICT_authorID_minYear_awardYear.keys():
            DICT_authorID_minYear_awardYear[line[1]] = {
                'minYear': int(line[3]),
                'awardYear': int(line[7])
            }
        else:
            if DICT_authorID_minYear_awardYear[line[1]]['minYear'] > int(line[3]):
                DICT_authorID_minYear_awardYear[line[1]] = {
                    'minYear': int(line[3]),
                     'awardYear': int(line[7])
                }
    pass

cnt = 0  # 看有没有负值
path2 = r"E:\FengXu\result\authorID_minYear_awardYear_academicAge.txt"
with open(path2, 'w', encoding='utf-8') as f:
    for authorID, minYear_awardYear in DICT_authorID_minYear_awardYear.items():
        academicAge = minYear_awardYear['awardYear'] - minYear_awardYear['minYear']
        if academicAge < 0:
            cnt = cnt + 1
        f.write(authorID+'\t'+minYear_awardYear['minYear']+'\t'+minYear_awardYear['awardYear']+'\t'+academicAge+'\n')
    pass
