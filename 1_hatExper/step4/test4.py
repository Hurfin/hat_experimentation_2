# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path1 = r"C:\Users\12433\Desktop\data11years\jq\affID_sortedName_fieldID_fieldName_HIndex(11years).txt"
path2 = r"C:\Users\12433\Desktop\data11years\jq\affID_sortedName_fieldID_fieldName_paperCnt(11years).txt"
path3 = r"C:\Users\12433\Desktop\data11years\jq\affID_sortedName_JIF(11years).txt"
path4 = r"C:\Users\12433\Desktop\data11years\jq\affID_sorteName_fieldID_fieldName_aveCitation(11years).txt"
path5 = r"C:\Users\12433\Desktop\data11years\jq\affID_sorteName_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt"
path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\jq.txt"

flag_ = True
jq_set = set()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if flag_ is True:
            flag_ = False
            continue
        jq_set.add((line[0], line[1]))
        pass
    pass

pathOut1 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_fieldID_fieldName_HIndex(11years).txt"
outer = open(pathOut1, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if (line[0], line[1]) in jq_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut2 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_fieldID_fieldName_paperCnt(11years).txt"
outer = open(pathOut2, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if (line[0], line[1]) in jq_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut3 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_JIF(11years).txt"
outer = open(pathOut3, 'w', encoding='utf-8')
with open(path3, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if (line[0], line[1]) in jq_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut4 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sorteName_fieldID_fieldName_aveCitation(11years).txt"
outer = open(pathOut4, 'w', encoding='utf-8')
with open(path4, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if (line[0], line[1]) in jq_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut5 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sorteName_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt"
outer = open(pathOut5, 'w', encoding='utf-8')
with open(path5, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if (line[0], line[1]) in jq_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()
