# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
查看还有多少期刊的JIF需要计算
"""
import pandas as pd
import csv
path1 = r"E:\FengXu\result1\fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear.txt"
path2 = r"E:\FengXu\result\JIF\JieqingContribute_JournalID.txt"
jq_journalID_set = set()
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').strip('.0')
        jq_journalID_set.add(line)
    pass

coAuthor_journalID_set = set()
flag = True
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if flag is True:
            flag = False
            continue
        if line[4] == '#':
            continue
        coAuthor_journalID_set.add(line[4])
        pass
    pass

print(len(jq_journalID_set), len(coAuthor_journalID_set))
print(len(coAuthor_journalID_set - jq_journalID_set))

coAuthor_journalID_needToComputeJIF = list(coAuthor_journalID_set - jq_journalID_set)
path_out1 = r"E:\FengXu\result1\coAuthorJournalID(needToCompute).txt"
with open(path_out1, 'w', encoding='utf-8') as f:
    for x in coAuthor_journalID_needToComputeJIF:
        f.write(x+'\n')
