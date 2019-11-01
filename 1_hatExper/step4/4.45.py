# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找对照组的前后合作密度（以及前后的合作者数量变化）
r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID.txt"

"""
import pandas as pd
path0 = r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID.txt"
path1 = r"D:\Dataset\NEW_MAG\Authors.txt"
dzCoAuthorID_set = set()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        dzCoAuthorID_set.add(line[1])
    pass
outer = open(r"E:\FengXu\result3\dzCoAuthorID_normalizedName.txt", 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[0] in dzCoAuthorID_set:
            outer.write(line[0]+'\t'+line[2]+'\n')
        pass
outer.close()
