import csv
import pandas as pd
import os
from collections import defaultdict
"""
# 杰青组文件
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years).txt"
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt"
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt"
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_HIndex(11years).txt"
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_paperCnt(11years).txt"
"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_JIF(11years).txt"
# 对照组文件
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_fieldID_fieldName.txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(buChuYiLunWenShu).txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_hindex11years.txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_jif11Years.txt"
"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_PaperCnt11Years.txt"
"""
def getLeftDzList(del_DZ_num, dz_FXID_prScore, dz_fieldID_Name_fxIDs_list):
    fxID_score = list()
    for fxID_i in dz_fieldID_Name_fxIDs_list:
        fxID_score.append([fxID_i, dz_FXID_prScore[fxID_i]])
    fxID_score = sorted(fxID_score, key=lambda x: x[1])
    print(fxID_score)
    ans_ = list()
    for i in range(0, len(fxID_score) - del_DZ_num):
        fxID_score_i = fxID_score[i]
        ans_.append(fxID_score_i[0])
    return ans_
    pass
def getLeftJqList(del_JQ_num, jq_affID_Name_prScore, jq_fieldID_Name_affID_SortedNames_list):
    jq_score = list()
    for jq_i in jq_fieldID_Name_affID_SortedNames_list:
        jq_score.append([jq_i, jq_affID_Name_prScore[jq_i]])
    jq_score = sorted(jq_score, key=lambda x: x[1])
    print(jq_score)
    ans_ = list()
    for i in range(0, len(jq_score) - del_JQ_num):
        jq_score_i = jq_score[i]
        ans_.append(jq_score_i[0])
    return ans_
    pass
path1 = r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_fieldID_fieldName.txt"
path2 = r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_paperCnt(11years).txt"

dz_fieldID_Name_cnt = defaultdict(lambda: 0)
jq_fieldID_Name_cnt = defaultdict(lambda: 0)

dz_fieldID_Name_fxIDs = defaultdict(lambda: [])
jq_fieldID_Name_affID_SortedNames = defaultdict(lambda: [])

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        dz_fieldID_Name_cnt[(line[1], line[2])] += 1
        dz_fieldID_Name_fxIDs[(line[1], line[2])].append(line[0])
    pass
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        jq_fieldID_Name_cnt[(line[5], line[6])] += 1
        jq_fieldID_Name_affID_SortedNames[(line[5], line[6])].append((line[0], line[1]))
    pass

dz_ = list()
for k, v in dz_fieldID_Name_cnt.items():
    dz_.append([k, v])
    pass
jq_ = list()
for k, v in jq_fieldID_Name_cnt.items():
    jq_.append([k, v])
    pass

dz_ = sorted(dz_, key=lambda x: x[0][0]+x[0][1])
jq_ = sorted(jq_, key=lambda x: x[0][0]+x[0][1])

print(dz_)
print(jq_)

# 给每个人都计算一个被删除的优先级数值，谁大就优先被删除掉
dz_FXID_prScore = defaultdict()
jq_affID_Name_prScore = defaultdict()
path3 = r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
path4 = r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"
flag = 1
with open(path3, 'r', encoding='utf-8') as f:
    for line in f:
        if flag == 1:
            flag = 0
            continue
        line = line.strip('\n').split('\t')
        coAuthorsNumBF = float(int(line[6]))
        coAuthorsNumAF = float(int(line[7]))
        score_i = abs((coAuthorsNumBF - coAuthorsNumAF) / (coAuthorsNumBF + 1))
        jq_affID_Name_prScore[(line[0], line[1])] = score_i
        pass
    pass
flag = 1
with open(path4, 'r', encoding='utf-8') as f:
    for line in f:
        if flag == 1:
            flag = 0
            continue
        line = line.strip('\n').split('\t')
        coAuthorsNumBF = float(int(line[5]))
        coAuthorsNumAF = float(int(line[6]))
        score_i = abs((coAuthorsNumBF - coAuthorsNumAF) / (coAuthorsNumBF + 1))
        dz_FXID_prScore[line[0]] = score_i
        pass
    pass
# 删除掉
path_root = "C:\\桌面文件\\代码_数据\\data11years\\test\\"
fOut1 = open(r"C:\桌面文件\代码_数据\data11years\test\jq_list.txt", 'w', encoding='utf-8')
fOut2 = open(r"C:\桌面文件\代码_数据\data11years\test\dz_list.txt", 'w', encoding='utf-8')
for i in range(0, len(dz_)):  # 循环每个领域
    dz_i = dz_[i]
    jq_i = jq_[i]
    fieldID_Name = dz_i[0]  # 领域ID, 领域Name
    dz_peopleNum = dz_i[1]
    jq_peopleNum = jq_i[1]

    jq_filter = []
    dz_filter = []

    if dz_peopleNum > jq_peopleNum:  # 如果对照组的人数多
        del_DZ_num = dz_peopleNum - jq_peopleNum
        fxIDsLeft = getLeftDzList(del_DZ_num, dz_FXID_prScore, dz_fieldID_Name_fxIDs[fieldID_Name])

        dz_filter = fxIDsLeft
        jq_filter = jq_fieldID_Name_affID_SortedNames[fieldID_Name]
        pass
    elif dz_peopleNum < jq_peopleNum:  # 如果杰青组的人数多
        del_JQ_num = jq_peopleNum - dz_peopleNum
        jqsLeft = getLeftJqList(del_JQ_num, jq_affID_Name_prScore, jq_fieldID_Name_affID_SortedNames[fieldID_Name])

        dz_filter = dz_fieldID_Name_fxIDs[fieldID_Name]
        jq_filter = jqsLeft
        pass
    else:
        dz_filter = dz_fieldID_Name_fxIDs[fieldID_Name]
        jq_filter = jq_fieldID_Name_affID_SortedNames[fieldID_Name]
        pass
    if len(dz_filter) != len(jq_filter):
        print("error!")
        os.system("pause")

    for jqAFFID_Name in jq_filter:
        fOut1.write(jqAFFID_Name[0]+'\t'+jqAFFID_Name[1]+'\t'+fieldID_Name[0]+'\t'+fieldID_Name[1]+'\n')
        pass
    for fxID in dz_filter:
        fOut2.write(fxID+'\t'+fieldID_Name[0]+'\t'+fieldID_Name[1]+'\n')
        pass
    pass
fOut1.close()
fOut2.close()
