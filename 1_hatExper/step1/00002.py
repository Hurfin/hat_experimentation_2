# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
将各个领域的杰青整合到一起
"""
import os
import pandas as pd
import csv
path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq"
fields_ = os.listdir(path0)
# print(fields_[0].rstrip('.txt').split('_'))
fields_ID_Name = []
for i in range(0, len(fields_)):
    fields_ID_Name.append(fields_[i].rstrip('.txt').split('_'))

all_JQ = []
for fname in fields_:
    path_i = path0 + "\\" + fname
    with open(path_i, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for list in reader:
            x = fname.rstrip('.txt').split('_')
            x = list + x
            all_JQ.append(x)

pathOut = r"E:\pythonCode\RJ_experimentation_1\Data_1\field\affID_sortedName_fieldID_fieldName.txt"
with open(pathOut, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f,delimiter='\t')
    for one in all_JQ:
        writer.writerow(one)
