import pandas as pd
import os
import csv
from collections import defaultdict

# 杰青组文件
jq_paths = [
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt",

    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_HIndex(11years).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_paperCnt(11years).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter1\affID_sortedName_LMH_JIF(11years).txt"
]
jq_paths_out = [
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt",

    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_fieldID_fieldName_HIndex(11years).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_fieldID_fieldName_paperCnt(11years).txt",
    r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_JIF(11years).txt"
]
# 对照组文件
dz_paths = [
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt",

    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_fieldID_fieldName.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(buChuYiLunWenShu).txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_hindex11years.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_jif11Years.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter1\fxID_LMH_PaperCnt11Years.txt"
]
dz_paths_out = [
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt",

    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\fxID_fieldID_fieldName.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(buChuYiLunWenShu).txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\fxID_LMH_hindex11years.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\fxID_LMH_jif11Years.txt",
    r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\fxID_LMH_PaperCnt11Years.txt"
]
path1 = r"C:\桌面文件\代码_数据\data11years\test\jq_list.txt"
path2 = r"C:\桌面文件\代码_数据\data11years\test\dz_list.txt"
jq_set = set()
dz_set = set()

jq_fieldCnt = defaultdict(lambda: 0)
dz_fieldCnt = defaultdict(lambda: 0)

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        jq_set.add((line[0], line[1]))
        jq_fieldCnt[(line[2], line[3])] += 1
    pass
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        dz_set.add(line[0])
        dz_fieldCnt[(line[1], line[2])] += 1
    pass
jq_field_cnt = []
dz_field_cnt = []
for k, v in jq_fieldCnt.items():
    jq_field_cnt.append([k, v])
for k, v in dz_fieldCnt.items():
    dz_field_cnt.append([k, v])
print(sorted(jq_field_cnt, key=lambda x: x[0][0]+x[0][1]))
print(sorted(dz_field_cnt, key=lambda x: x[0][0]+x[0][1]))

for i in range(0, len(jq_paths)):
    jq_path_in = jq_paths[i]
    jq_path_out = jq_paths_out[i]
    with open(jq_path_out, 'w', encoding='utf-8') as fout:
        flag = 1
        with open(jq_path_in, 'r', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip('\n').split('\t')
                if (i == 1 or i == 0) and (flag == 1):
                    flag = 0
                    fout.write('\t'.join(line)+'\n')
                    continue
                if (line[0], line[1]) in jq_set:
                    fout.write('\t'.join(line)+'\n')
                    pass
            pass
        pass
    pass

for i in range(0, len(dz_paths)):
    dz_path_in = dz_paths[i]
    dz_path_out = dz_paths_out[i]
    with open(dz_path_out, 'w', encoding='utf-8') as fout:
        flag = 1
        with open(dz_path_in, 'r', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip('\n').split('\t')
                if (i == 1 or i == 0) and (flag == 1):
                    flag = 0
                    fout.write('\t'.join(line)+'\n')
                    continue
                if line[0] in dz_set:
                    fout.write('\t'.join(line)+'\n')
                    pass
            pass
        pass
    pass
