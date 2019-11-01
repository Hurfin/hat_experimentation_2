# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组的前后合作密度（以及前后的合作者数量变化）
"""
import pandas as pd

path0 = r"E:\FengXu\result3\dzCoAuthorID_normalizedName.txt"
path1 = r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID.txt"

dzCoAuthorID_normalizedName_dict = dict()

with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        dzCoAuthorID_normalizedName_dict[line[0]] = line[1]

outer = open(r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt", 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in dzCoAuthorID_normalizedName_dict.keys():
            outer.write('\t'.join(line)+'\t'+dzCoAuthorID_normalizedName_dict[line[1]]+'\n')
        else:
            print(line)
    pass
outer.close()
