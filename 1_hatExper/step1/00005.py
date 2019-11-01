# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
续上找到引用者的paper year
（已经有id和ref id了，找id的paper year）
"""
import pandas as pd
import os
import numpy
import csv

path_papers = r"D:\Dataset\NEW_MAG\Papers.txt"
path_ref = r"E:\FengXu\result1\paperReferences(refJQ).txt"

paperID_set = set()
with open(path_ref, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        paperID_set.add(line[0])
path_out = r"E:\FengXu\tmp\paperID_paperYear.txt"
outer = open(path_out, 'w', encoding='utf-8')
with open(path_papers, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        # line[0], line[7]
        if line[7] == '' or line[7] is None:
            continue
        if line[0] in paperID_set:
            outer.write(line[0]+'\t'+line[7]+'\n')
            pass
outer.close()
