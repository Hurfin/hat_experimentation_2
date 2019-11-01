# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""

"""
import pandas as pd
path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\dz.txt"

flag_ = True
dz_fxID_set = set()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if flag_ is True:
            flag_ = False
            continue
        dz_fxID_set.add(line[0])
        pass
    pass

path1 = r"C:\Users\12433\Desktop\data11years\dz\(coAuthor)fxID_hindex11years.txt"
path2 = r"C:\Users\12433\Desktop\data11years\dz\(coAuthor)fxID_jif11Years.txt"
path3 = r"C:\Users\12433\Desktop\data11years\dz\(coAuthor)fxID_PaperCnt11Years.txt"
path4 = r"C:\Users\12433\Desktop\data11years\dz\fxID_assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt"
path5 = r"C:\Users\12433\Desktop\data11years\dz\fxID_assumeAwardYear_minYear_aveCitationCnt11years(buChuYiLunWenShu).txt"

pathOut1 = r"C:\Users\12433\Desktop\data11years\dz\filter\(coAuthor)fxID_hindex11years.txt"
outer = open(pathOut1, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in dz_fxID_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut2 = r"C:\Users\12433\Desktop\data11years\dz\filter\(coAuthor)fxID_jif11Years.txt"
outer = open(pathOut2, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in dz_fxID_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut3 = r"C:\Users\12433\Desktop\data11years\dz\filter\(coAuthor)fxID_PaperCnt11Years.txt"
outer = open(pathOut3, 'w', encoding='utf-8')
with open(path3, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in dz_fxID_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut4 = r"C:\Users\12433\Desktop\data11years\dz\filter\fxID_" \
           r"assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt"
outer = open(pathOut4, 'w', encoding='utf-8')
with open(path4, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in dz_fxID_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()

pathOut5 = r"C:\Users\12433\Desktop\data11years\dz\filter\fxID_assumeAwardYear_minYear_" \
           r"aveCitationCnt11years(buChuYiLunWenShu).txt"
outer = open(pathOut5, 'w', encoding='utf-8')
with open(path5, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in dz_fxID_set:
            outer.write('\t'.join(line)+'\n')
    pass
outer.close()
