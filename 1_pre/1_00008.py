# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
E:\FengXu\Data\awardYear_englishName_affID_chineseName.txt

'awardYear', 'englishName', 'affiliationID', 'chineseName'
'paperID', 'authorID', 'affiliationID', 'paperYear', 'normalizedName', 'displayName'
"""
import pandas as pd
import os
import copy
def is_nameMatched(normalizedName, displayName, englishName, chineseName):
    """姓在前 姓在后 中文名"""
    name_i = englishName.split(" ")
    if len(name_i) > 2:
        print(name_i)
        os.system("pause")
    name1 = ""
    name2 = ""
    if len(name_i) == 2:
        name1 = name_i[0].lower() + " " + name_i[1].lower()
        name2 = name_i[1].lower() + " " + name_i[0].lower()
    if len(name_i) == 1:
        name1 = name_i[0].lower()
        name2 = name_i[0].lower()
    if normalizedName == chineseName:
        return True
    if normalizedName == name1 or normalizedName == name2:
        # 检查displayName中是不是有中文名
        flag_has_chinese = False
        for i in displayName:
            if i>=u'\u4e00' and i<=u'\u9fff':
                flag_has_chinese = True
                break
        if flag_has_chinese == True:  # 如果displayName中有中文名
            if chineseName in displayName:
                return True
            else:
                return False
        return True
    return False
    pass


path1 = r"E:\FengXu\Data\awardYear_englishName_affID_chineseName.txt"
path2 = r"E:\FengXu\result\1_JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.txt"
awardYear_englishName_affID_chineseName = []
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        line[0] = int(line[0])  # awardYear
        line[2] = float(line[2])  # affiliation id
        awardYear_englishName_affID_chineseName.append(line)

JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName = []
with open(path2, "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        line[2] = float(line[2])  # affiliation id
        line[3] = int(float(line[3]))  # paper year
        JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.append(line)

before_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i = []
matched_List = []
for i in range(0, len(JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName)):

    for j in range(0, len(awardYear_englishName_affID_chineseName)):
        paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i = \
            copy.deepcopy(JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName[i])

        awardYear_englishName_affID_chineseName_j = awardYear_englishName_affID_chineseName[j]
        # 如果名字对的上，而且affID也对的上，就先认为是匹配上了
        if paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i[2] != awardYear_englishName_affID_chineseName_j[2]:  # 机构ID是否匹配
            continue
        normalizedName = paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i[4]
        displayName = paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i[5]
        englishName = awardYear_englishName_affID_chineseName_j[1]
        chineseName = awardYear_englishName_affID_chineseName_j[3]
        if is_nameMatched(normalizedName, displayName, englishName, chineseName) is False:  # 看名字是否匹配
            continue

        # 都匹配上的话，就保存这个
        paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear = \
            copy.deepcopy(paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i)
        paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.append(
            awardYear_englishName_affID_chineseName_j[3]
        )
        paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.append(
            awardYear_englishName_affID_chineseName_j[0]
        )
        matched_List.append(
            paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear
        )
        if len(paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear)!=8:
            print(">8_award", paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear)
            print("displayName", paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i)
            print("before displayName", before_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i)
            os.system("pause")
        before_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i = paperID_authorID_affiliationID_paperYear_normalizedName_displayName_i
        pass
    pass

# pathOut = r"E:\FengXu\result\JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"
pathOut2 = r"E:\FengXu\result\3_JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"

exception_path = r"E:\FengXu\result\exception.txt"
f_exception = open(exception_path, 'w', encoding='utf-8')

with open(pathOut2, "w", encoding='utf-8') as f:
    # JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear
    for x in matched_List:
        x[2] = str(int(x[2]))
        x[3] = str(int(x[3]))
        x[7] = str(x[7])
        try:
            xx = '\t'.join(x)
            f.write(xx + '\n')
        except Exception as e:
            print(e)
            print(x)
            flag = 1
            for i in x:
                if flag == 1:
                    f_exception.write(str(i))
                    flag = 0
                else:
                    f_exception.write('\t'+str(i))
            f_exception.write('\n')
f_exception.close()
