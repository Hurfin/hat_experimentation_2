# -*- coding: utf-8 -*-
# !/usr/bin/env python
import functools


def cmp(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    return 0
    pass


orgHas_englishName = []
orgHasNot_englishName = []

with open(r"E:\pythonCode\RJ_experimentation_1\Data\orgName_englishName.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        if len(line) > 1:
            orgHas_englishName.append(line)
            pass
        else:
            orgHasNot_englishName.append(line)
            pass
    pass
l = []
n = []
for org in orgHas_englishName:
    if "中国科学院" in org[0]:
        l.append([org[0], 'Chinese Academy of Sciences'])
    else:
        l.append(org)
    pass

for org in orgHasNot_englishName:
    if "中国科学院" in org[0]:
        l.append([org[0], 'Chinese Academy of Sciences'])
    else:
        n.append(org)

l = sorted(l, key=functools.cmp_to_key(cmp))
print(l)
print(n)



with open(r"E:\pythonCode\RJ_experimentation_1\Data\orgFormatName.txt", "w", encoding='utf-8') as f:
    for org in l:
        f.write('\t'.join(org)+"\n")
    for org in n:
        f.write(org[0]+'\n')
    pass
