# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\affID_sortedName_coAuthors.txt"

将其中的一个（affID, sortedName）对应有多个coAuthorID的数据删除掉，只保留合并后有一个coAuthorID的这些人
"""
import pandas as pd
import csv

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\affID_sortedName_coAuthors.txt"
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\affID_sortedName_coAuthorID(drop_multi_CoAuthorID).txt"
outer = open(path_out, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if len(line) > 3:
            continue
        outer.write('\t'.join(line)+'\n')
    pass
outer.close()
