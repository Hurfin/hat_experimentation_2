# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
先整理数据然后下一个程序
计算aveCitation
（先用整理出来的这部分杰青来算citation，这部分杰青都比较全）
（后面可以跟之前算好的jif、papercnt、hIndex进行合并）

"""
import pandas as pd
import os
import csv
"""
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\JQ_" \
        r"affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"

data = pd.read_csv(path1, sep='\t', header=None, usecols=[4])
data = data.drop_duplicates()

pathOut = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\jq_paperIDs.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)  # 得到了杰青的所有paper id
"""

path_ref = r"D:\Dataset\NEW_MAG\PaperReferences.txt"
path_jqPaperID = r"E:\FengXu\tmp\jq_paperIDs.txt"
path_out = r"E:\FengXu\result1\paperReferences(refJQ).txt"
jq_paperID_set = set()
# 得到杰青paper id的集合
with open(path_jqPaperID, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        jq_paperID_set.add(line)

outer = open(path_out, 'w', encoding='utf-8')
with open(path_ref, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in jq_paperID_set:
            outer.write(line[0]+'\t'+line[1]+'\n')
outer.close()



