# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
coAuthor的四个参数
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthorCombined)\(coAuthor)
fxID_assumeAwardYear_minYear_bf_jif_bf_aveCitation_bf_hindex_bf_paperCnt_
af_jif_af_aveCitation_af_hindex_af_paperCnt(chuYiLunWenShu).txt"

杰青的参数
r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_
bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_af_avejif_af_avecitation_af_avehindex_af_avepapercnt(buChuYi).txt"

r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_
bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_af_avejif_af_avecitation_af_avehindex_af_avepapercnt(chuYi).txt"

给每个杰青找对照的人，条件是：同minYear下，欧氏距离最近的
有几个杰青没有找到对照组，可能没有对应的minYear的coAuthor了吧
取出这部分杰青，给他们找个minYear比较接近的、没使用过的coAuthor作为对照组就行了。
"""
import pandas as pd
import os
import math
import numpy as np


def getOneCompare(jq_i, sameMinYearCoAuthors, usedCoAuthor):
    # 返回一个未使用过的、与该杰青欧氏距离最接近的 fxID。（如果已经没有可以选择的coAuthor的话，就返回None）
    # return [fxID, dist] or None
    if sameMinYearCoAuthors.shape[0] == 0 or sameMinYearCoAuthors is None:
        return None
    jq_bfJIF = jq_i['bf_avejif']
    jq_bfAveCitation = jq_i['bf_avecitation']
    jq_bfhindex = jq_i['bf_avehindex']
    jq_bfAvePaperCnt = jq_i['bf_avepapercnt']
    sameMinYearCoAuthors = sameMinYearCoAuthors.astype(
        {'fxID': str, 'assumeAwardYear': int, 'minYear': int,
         'bf_jif': float, 'bf_aveCitation': float, 'bf_hindex': float, 'bf_paperCnt': float,
         'af_jif': float, 'af_aveCitation': float, 'af_hindex': float, 'af_paperCnt': float}
    )
    sameMinYearCoAuthors['dist'] = sameMinYearCoAuthors.apply(
        lambda x: math.sqrt((x['bf_jif']-jq_bfJIF)**2 + (x['bf_aveCitation']-jq_bfAveCitation)**2 +
                            (x['bf_hindex']-jq_bfhindex)**2 + (x['bf_paperCnt']-jq_bfAvePaperCnt)**2), axis=1)
    sameMinYearCoAuthors = sameMinYearCoAuthors[['fxID', 'dist']]
    sameMinYearCoAuthors = sameMinYearCoAuthors.dropna()
    # sameMinYearCoAuthors =sameMinYearCoAuthors.sort_values(by=['dist'], ascending=True)
    # for i_ in range(0, len(sameMinYearCoAuthors)):
    #     fxID_i = str(sameMinYearCoAuthors.iloc[i]['fxID'])
    #     dist_i = float(sameMinYearCoAuthors.iloc[i]['dist'])
    #     if fxID_i not in usedCoAuthor:
    #         return [fxID_i, dist_i]
    # return None
    # sameMinYearCoAuthors = list(sameMinYearCoAuthors)
    sameMinYearCoAuthors = np.array(sameMinYearCoAuthors).tolist()
    # print("OK", sameMinYearCoAuthors)
    sorted(sameMinYearCoAuthors, key=lambda x: x[1])
    for x_i in sameMinYearCoAuthors:
        fxID_i = str(x_i[0])
        dist_i = float(x_i[1])
        if fxID_i not in usedCoAuthor:
            return [fxID_i, dist_i]
    return None


path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
        r"(affID_sortedName)\4\(coAuthorCombined)\(coAuthor)" \
        r"fxID_assumeAwardYear_minYear_bf_jif_bf_aveCitation_bf_hindex_bf_paperCnt_" \
        r"af_jif_af_aveCitation_af_hindex_af_paperCnt(chuYiLunWenShu).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_awardYear_fieldID_fieldName_" \
        r"bf_avejif_bf_avecitation_bf_avehindex_bf_avepapercnt_" \
        r"af_avejif_af_avecitation_af_avehindex_af_avepapercnt(chuYi).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1\affID_sortedName_minYear.txt"
# fxID	assumeAwardYear	minYear
# bf_jif	bf_aveCitation	bf_hindex	bf_paperCnt
# af_jif	af_aveCitation	af_hindex	af_paperCnt
data1 = pd.read_csv(path1, sep='\t')  # coAuthor
# affID	sortedName	awardYear	fieldID	fieldName
# bf_avejif	bf_avecitation	bf_avehindex bf_avepapercnt
# af_avejif	af_avecitation	af_avehindex  af_avepapercnt
data2 = pd.read_csv(path2, sep='\t')  # 杰青
# affID	sortedName	minYear
data3 = pd.read_csv(path3, sep='\t')  # 杰青的minYear
data2 = pd.merge(data2, data3, on=['affID', 'sortedName'], how='inner')
# print(data2.columns)
del data3
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\(jq_coAuthor)compareGroup\affID_sortedName_fxID_dist.txt"
outer = open(path_out, 'w', encoding='utf-8')
usedCoAuthor = set()  # 已经用过的coAuthor
notOK_jq = []  # 没找到对照的coAuthor的杰青
dist_list = []
cnt = 0
for i in range(0, data2.shape[0]):  # 循环每个杰青
    jq_i = data2.iloc[i]  # 取出一个杰青
    jq_i_minYear = jq_i['minYear']  # 该杰青的minYear
    sameMinYearCoAuthors = data1[data1['minYear'] == jq_i_minYear]  # 和这个杰青相同minYear的coAuthors
    compareOne = getOneCompare(jq_i, sameMinYearCoAuthors, usedCoAuthor)  # 如果找到一个合适的对照组的话就返回[fxID, dist] or None
    if compareOne is None:
        # print('no comp\n', jq_i['affID'], jq_i['sortedName'])
        print(jq_i['affID'], jq_i['sortedName'], jq_i['minYear'])
        notOK_jq.append(jq_i)
    else:
        outer.write(str(jq_i['affID'])+'\t'+str(jq_i['sortedName'])+'\t'+str(compareOne[0])+'\t'+str(compareOne[1])+'\n')
        usedCoAuthor.add(compareOne[0])  # 这个fxID已经用过了
        dist_list.append(compareOne[1])
        cnt += 1
    pass
outer.close()

print(min(dist_list), max(dist_list))
print(cnt)
#
# test = data1[data1['minYear'] == 2011]
# test = test[~test.fxID.isin(list(usedCoAuthor))]
# print(test.shape[0])
# print(max(list(data1['minYear'])))
# # data1 = data1[~data1.fxID.isin(list(usedCoAuthor))]
# for x in notOK_jq:
#     roundMinYearCoAuthors = data1[abs(data1['minYear'] - x['minYear']) <= 5]
#     compareOne_i = getOneCompare(x, roundMinYearCoAuthors, usedCoAuthor)
#     if compareOne_i is None:
#         print(x['affID'], x['sortedName'], x['minYear'])
#     else:
#         outer.write(str(x['affID'])+'\t'+str(x['sortedName'])+'\t'+str(compareOne_i[0])+'\t'+str(compareOne_i[1])+'\n')
#         usedCoAuthor.add(compareOne_i[0])
#         dist_list.append(compareOne_i[1])
#     pass
# outer.close()
