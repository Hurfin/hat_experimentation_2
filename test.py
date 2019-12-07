# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd

path = r"C:\Users\12433\Desktop\a\new\ans_CII(flag_before_1_after_0).txt"

set_ = set()
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n').split('\t')
        set_.add((line[0], line[1]))
print(set_.__len__())
print(list(set_)[0])

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveCitationCntPerYear(before5ANDafter5).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveJIFPerYear(before5ANDafter5).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_h-IndexPerYear(before5ANDafter5).txt"
path4 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_paperCntPerYear(Before5ANDafter5).txt"

path5 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment3_result\1result\collaboratorsBeforeAndAfter5year.txt"
