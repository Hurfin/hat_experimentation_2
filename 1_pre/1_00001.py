# -*- coding: utf-8 -*-
# !/usr/bin/env python


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

with open(r"E:\pythonCode\RJ_experimentation_1\Data\orgHas_englishName.txt", "w", encoding='utf-8') as f:
    for org in orgHas_englishName:
        f.write('\t'.join(org)+"\n")
    pass

with open(r"E:\pythonCode\RJ_experimentation_1\Data\orgHasNot_englishName.txt", "w", encoding='utf-8') as f:
    for org in orgHasNot_englishName:
        f.write(org[0]+"\n")
    pass
