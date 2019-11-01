# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
之前得到了coAuthorID, affID, sortedName

这里将其处理为（affID, sortedName）,coAuthorID_i
"""
import pandas as pd
import csv
from collections import defaultdict

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_" \
           r"sortedName)\coAuthorID_affID_sortedName.txt"

coAuthor_DICT = defaultdict(list)

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        coAuthor_DICT[(line[1], line[2])].append(line[0])
        pass
    pass
cnt = 0
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\affID_sortedName_coAuthors.txt"
with open(path_out, 'w', encoding='utf-8') as f:
    for k, v in coAuthor_DICT.items():
        f.write(k[0]+'\t'+k[1]+'\t'+'\t'.join(v)+'\n')
        if len(v) > 1:
            cnt += 1
        pass
    pass
print(len(coAuthor_DICT))
print(cnt)
