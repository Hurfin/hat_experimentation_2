# -*- coding: utf-8 -*-
# !/usr/bin/env python

# path1 = r"E:\pythonCode\RJ_experimentation_1\Data\awardYear_englishName_affID_chineseName.txt"
# # 找到杰青里面同机构、同英文名的
# sameOrg_englishName = []
# flag = set()
# with open(path1, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         line = line.split('\t')
#         if (line[1], line[2]) in flag:
#             sameOrg_englishName.append((line[1], line[2]))
#         else:
#             flag.add((line[1], line[2]))
#     pass
#
# for x in sameOrg_englishName:
#     print(x)

re_name = [
    ('jianping li', 'li jianping', '19820366'),
    ('lixin zhang', 'zhang lixin', '19820366'),
    ('peijun shi', 'shi peijun', '25254941'),
    ('haibo li', 'li haibo', '19820366'),
    ('ling chen', 'chen ling', '19820366'),
    ('bin liu', 'liu bin', '99065089'),
    ('jian xu', 'xu jian', '19820366')
]
path1 = r"E:\FengXu\result\4_JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"
path4 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_JieQing_paperID_authorID_affiliationID_paperYear_normalizedName_displayName_chineseName_awardYear.txt"

fout = open(path4, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        flag = 0
        for i in range(0, len(re_name)):
            if line[2] == re_name[i][2] and (re_name[i][0] == line[4] or re_name[i][1] == line[4]):
                flag = 1
                break
        if flag == 1:
            continue
        else:
            fout.write('\t'.join(line)+'\n')
fout.close()