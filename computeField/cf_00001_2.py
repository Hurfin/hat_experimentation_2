# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
"""
import pandas as pd
import pickle as pkl
from collections import Counter


def getPaperField(fieldID_list, fatherFieldID_subFieldIDSet_dict):
    mapToFather_list = list()
    flag_find_paperField = 0
    for fieldID in fieldID_list:
        fieldID = str(fieldID)
        flag_find = 0
        for key, value in fatherFieldID_subFieldIDSet_dict.items():
            if (fieldID == key) or (fieldID in fatherFieldID_subFieldIDSet_dict[key]):
                mapToFather_list.append(key)
                flag_find_paperField = 1
                flag_find = 1
                break
        if flag_find == 0:
            print('not find this fieldID', fieldID)
    if flag_find_paperField == 0:
        print('not find this paperField')
    counter = Counter(mapToFather_list)
    print(counter.most_common(2))
    FFID = counter.most_common(1)[0][0]
    return FFID


path = r"E:\pythonCode\RJ_experimentation_1\Data\field\jq_paperID_fieldsID.txt"
path1 = r"E:\pythonCode\RJ_experimentation_1\subfields\subfields\fields.txt"
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\field\ans_paperID_fatherFieldID.txt"
fields_ = list()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fields_.append((line[0], line[1]))
# 建立father field id---sub field id set的字典
fatherFieldID_subFieldIDSet_dict = dict()
for fieldID_fieldName in fields_:
    pt = "E:/pythonCode/RJ_experimentation_1/subfields/subfields/" + "subfields_" + fieldID_fieldName[1] + ".txt"
    fatherFieldID_subFieldIDSet_dict[fieldID_fieldName[0]] = set()
    with open(pt, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            fatherFieldID_subFieldIDSet_dict[fieldID_fieldName[0]].add(line)
        pass

data = pd.read_csv(path, sep='\t', header=None, names=['paperID', 'fieldsID'])
data = data.groupby(['paperID'])
fout = open(pathOut, 'w', encoding='utf-8')
for paperID, group in data:
    paperFieldID = getPaperField(list(group['fieldsID']), fatherFieldID_subFieldIDSet_dict)
    fout.write(str(paperID)+'\t'+str(paperFieldID)+'\n')
    pass
fout.close()
