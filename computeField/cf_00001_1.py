# -*- coding: utf-8 -*-
# !/usr/bin/env python

path = r"E:\FengXu\result\TMP\tmp_data\jq_paperIDs.txt"
path1 = r"D:\Dataset\NEW_MAG\PaperFieldsOfStudy.txt"
set_ = set()
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        set_.add(line)
fout = open(r"E:\FengXu\result\TMP\tmp_data\jq_paperID_fieldsID.txt", 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in set_:
            fout.write(line[0]+'\t'+line[1]+'\n')
fout.close()
