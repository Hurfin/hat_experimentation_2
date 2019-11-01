# -*- coding: utf-8 -*-
# !/usr/bin/env python
org_eng = []  # chinese name, lower englishName
with open(r"E:\pythonCode\RJ_experimentation_1\Data\orgFormatName.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        if len(line) > 1:
            tmp_list = []
            for i in range(0, len(line)):
                tmp_list.append(line[i].lower())
            org_eng.append(tmp_list)
    pass

orgID_normalizeName = []  # org id, normalize name
with open(r"E:\pythonCode\RJ_experimentation_1\Data\Affiliations.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        orgID_normalizeName.append([line[0], line[2]])
    pass

notMatchOrg = []
f = open(r"E:\pythonCode\RJ_experimentation_1\Data\orgID_orgName_part1.txt", "w", encoding='utf-8')  # 先处理能够英文名字直接对上的
for orgChineseName_lowerEnglishName in org_eng:
    flag = False  # 是否能找到直接匹配上的
    for orgID_normalizeEnglishName in orgID_normalizeName:
        # print(orgChineseName_lowerEnglishName[1], orgID_normalizeEnglishName[1])
        if orgChineseName_lowerEnglishName[1] == orgID_normalizeEnglishName[1]:
            print(orgID_normalizeEnglishName[0]+"\t"+orgChineseName_lowerEnglishName[0]+"\t"+orgID_normalizeEnglishName[1])
            f.write(orgID_normalizeEnglishName[0]+"\t"+orgChineseName_lowerEnglishName[0]+"\t"+orgID_normalizeEnglishName[1]+"\n")
            flag = True
    if flag is False:
        notMatchOrg.append(orgChineseName_lowerEnglishName)
f.close()

# 把英文名不能直接对上的，挑选出来
f = open(r"E:\pythonCode\RJ_experimentation_1\Data\notMatchOrg.txt", "w", encoding='utf-8')
for x in notMatchOrg:
    f.write('\t'.join(x)+"\n")
f.close()
