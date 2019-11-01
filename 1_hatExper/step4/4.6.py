# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
剔除掉杰青的author id，把剩下的co-author的 id 也按sortedName和affID合并

这里先整理出来剔除掉杰青author id后的author id的数据，下一步对这部分得到的数据进行相同sortedName，affID合并操作
"""
import pandas as pd
import os
import csv

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\杰青论文id下的所有作者" \
          r"以及机构数据\filterCN_jqPaperID_authorID_affID.txt"

set_ = set()  # 所有的author id（包括jq的和jq的合作者的）
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        set_.add(line[1])
print('所有的author id', len(set_))

path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\filtered_JQ_affiliationID_sortedName_" \
        r"fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
set_jqID = set()  # jq的author id
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        set_jqID.add(line[5])
    pass
print('杰青的author id', len(set_jqID))

set_ = set_ - set_jqID
co_authorIDs = list(set_)
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_authorIDs\co_authorIDs.txt"
with open(path_out, 'w', encoding='utf-8') as f:
    for authorID in co_authorIDs:
        f.write(authorID+'\n')
    pass
