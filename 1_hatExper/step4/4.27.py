# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
已有
r"E:\FengXu\result\JIF\(coAuthorNeedToCompute)journalID_JIF_perYear_from1989to2017.txt"

把他和之前计算过的期刊的JIF
（r"E:\pythonCode\RJ_experimentation_1\Data\result\JIFfrom1989to2017_MAG_JieqingContributeJournal\journalID_JIF_perYear_from1989to2017.txt"）
整合到一起
"""
import pandas as pd
import csv
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\JIF\(coAuthorNeedToCompute)" \
        r"journalID_JIF_perYear_from1989to2017.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\result\JIFfrom1989to2017_MAG_" \
        r"JieqingContributeJournal\journalID_JIF_perYear_from1989to2017.txt"

path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\JIF\(all)" \
           r"journalID_JIF_perYear_from1989to2017.txt"

ans_ = []
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        line[0] = line[0].rstrip('.0')
        ans_.append(line)
    pass

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        ans_.append(line)
    pass

with open(path_out, 'w', encoding='utf-8') as f:
    for l in ans_:
        f.write('\t'.join(l)+'\n')
