# -*- coding: utf-8 -*-
# !/usr/bin/env python
JieChuQingNian = []
with open(r"E:\pythonCode\RJ_experimentation_1\Data\杰出青年.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        JieChuQingNian.append(line)
    pass

orgID_orgName_englishName = []
with open(r"E:\pythonCode\RJ_experimentation_1\Data\orgID_orgName_part1.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        orgID_orgName_englishName.append(line)
    pass

people_has_orgID = []
people_hasNot_orgID = []

for people in JieChuQingNian:
    flag = True
    for org in orgID_orgName_englishName:
        # print(len(people), len(org))
        if people[4] == org[1]:
            x = people
            x.append(org[0])
            people_has_orgID.append(x)
            flag = False
        pass
    if flag is True:
        people_hasNot_orgID.append(people)
    pass
print(len(people_has_orgID), len(people_hasNot_orgID))

with open(r"E:\pythonCode\RJ_experimentation_1\Data\people_has_orgID.txt", "w", encoding='utf-8') as f:
    for people in people_has_orgID:
        f.write('\t'.join(people)+"\n")
    pass

with open(r"E:\pythonCode\RJ_experimentation_1\Data\people_hasNot_orgID.txt", "w", encoding='utf-8') as f:
    for people in people_hasNot_orgID:
        f.write('\t'.join(people)+"\n")
    pass
