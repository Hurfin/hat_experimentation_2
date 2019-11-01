# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
author name, affiliation id, paper year,
"""
DICT_author_minYear_awardYear = {}  # 一个author(相同name和相同的affiliation id)的最早发论文的年份
# path1 = r"E:\FengXu\result\JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"
path1 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"
# path 记得要修改

# 只保留一个作者(name, affiliation id相同的视为同一个人)最早发的论文的信息
FULL_doc = []
with open(path1, "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        FULL_doc.append(line)
        affID_normalized = line[2] + "\t" + line[4]  # affiliationID, normalizedName
        if affID_normalized not in DICT_author_minYear_awardYear.keys():
            DICT_author_minYear_awardYear[affID_normalized] = {
                'minYear': int(line[3]),
                'awardYear': int(line[7])
            }
        else:
            if DICT_author_minYear_awardYear[affID_normalized]['minYear'] > int(line[3]):
                DICT_author_minYear_awardYear[affID_normalized] = {
                    'minYear': int(line[3]),
                    'awardYear': int(line[7])
                }
    pass

cnt = 0  # 看有没有负值
path2 = r"E:\FengXu\result\1_affiliationID_authorEnglishName_minYear_awardYear_academicAge.txt"
with open(path2, 'w', encoding='utf-8') as f:
    for author_i, minYear_awardYear in DICT_author_minYear_awardYear.items():
        academicAge = minYear_awardYear['awardYear'] - minYear_awardYear['minYear']
        if academicAge < 0:
            cnt = cnt + 1
            continue
        f.write(author_i+'\t'+str(minYear_awardYear['minYear'])+'\t'+str(minYear_awardYear['awardYear'])+'\t'+str(academicAge)+'\n')
    pass
print(cnt)