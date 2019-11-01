# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
找dz.txt中fxID对应的领域

续上
已得到E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\coAuthorID_fxID_jqPaperIDs.txt

"""
import pandas as pd
import pickle as pkl
from collections import defaultdict
from collections import Counter
path0 = r"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\coAuthorID_fxID_jqPaperIDs.txt"

jqPaperIDs_need_set = set()
coAuthorID_FxID_jqPaperIDs_dict = dict()
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        for x in line[2:]:
            jqPaperIDs_need_set.add(x)
        coAuthorID_FxID_jqPaperIDs_dict[(line[0], line[1])] = line[2:]
        pass
    pass

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\JQ\filtered_" \
        r"JQ_affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
paperID_field_dict = defaultdict(lambda: [])
# affID	sortedName	fieldID	fieldName	paperID	authorID	paperYear	awardYear	citationCnt
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        paperID_field_dict[line[4]].append((line[2], line[3]))
        pass
    pass

for k, v in paperID_field_dict.items():
    paperID_field_dict[k] = list(set(v))
    pass
# cnt = 0
# for k, v in paperID_field_dict.items():
#     if len(v) > 1:
#         print(k, v)
#         cnt += 1
# print(cnt)
# outer = open(r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\fxID_fieldID_fieldName.txt", 'w', encoding='utf-8')
outer = open(r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\coAuthorID_fxID_fieldID_fieldName.txt", 'w', encoding='utf-8')
for k, v in coAuthorID_FxID_jqPaperIDs_dict.items():
    field_list = list()
    for x in v:  # for each jqPaperID
        field_list += (paperID_field_dict[x])
    C = Counter(field_list)
    print(k[1], C.most_common(1)[0][0][0], C.most_common(1)[0][0][1])
    outer.write(k[0]+'\t'+k[1]+'\t'+str(C.most_common(1)[0][0][0])+'\t'+str(C.most_common(1)[0][0][1])+'\n')
    pass
outer.close()
