# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
"E:\FengXu\result2\jqPaperID_coAuthorID_affID_normalizedName.txt"
"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\affID_sortedName_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
"""
import pandas as pd
path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\fxID_fieldID_fieldName.txt"
# fxID	assumeAwardYear	minYear	bf_jif	bf_citation	bf_hindex	bf_papercnt	L	M	H	af_jif	af_citation	af_hindex	af_papercnt
path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\dz.txt"

fxID_fieldID_fieldName_dict = dict()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fxID_fieldID_fieldName_dict[line[0]] = (line[1], line[2])
        pass
    pass

dz = []
flag_ = True
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if flag_ is True:
            dz.append(line)
            flag_ = False
            continue
        x1 = str(int(float(line[0])))
        x2 = str(int(float(line[1])))
        x3 = str(int(float(line[2])))
        dz.append([x1, x2, x3]+line[3:])
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\dz1.txt"
flag_ = True
with open(path2, 'w', encoding='utf-8') as f:
    for line in dz:
        if flag_ is True:
            flag_ = False
            f.write(line[0]+'\t'+"fieldID"+'\t'+"fieldName"+'\t'+'\t'.join(line[1:])+'\n')
            continue
        f.write(
            line[0] + '\t' + fxID_fieldID_fieldName_dict[line[0]][0] + '\t' + fxID_fieldID_fieldName_dict[line[0]][1] +
            '\t' + '\t'.join(line[1:]) + '\n')
        pass
    pass
