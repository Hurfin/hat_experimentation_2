# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
之前已经得到了jqPaperID, authorID, affiliationID

先把affiliationID是中国的筛选出来
得到机构为 CN 的jqPaperID, authorID, affiliationID
"""
import pandas as pd
import os
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\CN_affiliations\CN_affiliations.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\杰青论文id下的所" \
        r"有作者以及机构数据\jqPaperID_authorID_affID.txt"
CN_affID_set = set()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        CN_affID_set.add(line[1])

pathout = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\杰青论文id下的所有作者" \
          r"以及机构数据\filterCN_jqPaperID_authorID_affID.txt"
outer = open(pathout, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[2] in CN_affID_set:
            outer.write('\t'.join(line)+'\n')
outer.close()
