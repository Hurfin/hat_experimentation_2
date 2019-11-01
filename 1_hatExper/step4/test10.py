import pandas as pd
import csv
import os
from collections import defaultdict
path1 = r"C:\桌面文件\代码_数据\data11years\test\dz_list.txt"
path2 = r"C:\桌面文件\代码_数据\data11years\test\jq_list.txt"

dz_field_fxID = defaultdict(lambda: set())
jq_field_jqAfidName = defaultdict(lambda: set())

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        dz_field_fxID[(line[1], line[2])].add(line[0])
    pass
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        jq_field_jqAfidName[(line[2], line[3])].add((line[0], line[1]))
    pass

path3 = r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"
path4 = r"C:\桌面文件\代码_数据\data11years\dz\dz_filter2\dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt"
dz_out = "C:\\桌面文件\\代码_数据\\data11years\\dz\\dz_filter2\\dz_splitByField\\"
for field, fxIDs_set in dz_field_fxID.items():
    path_ = dz_out + field[0] + "_" + field[1] + "_" + "dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"
    with open(path_, 'w', encoding='utf-8') as fout:
        with open(path3, 'r', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip('\n').split('\t')
                if line[0] in fxIDs_set:
                    fout.write('\t'.join(line)+'\n')
    path__ = dz_out + field[0] + "_" + field[1] + "_" + "dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt"
    with open(path__, 'w', encoding='utf-8') as fout:
        with open(path4, 'r', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip('\n').split('\t')
                if line[0] in fxIDs_set:
                    fout.write('\t'.join(line)+'\n')


path5 = r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
path6 = r"C:\桌面文件\代码_数据\data11years\jq\jq_filter2\affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt"
jq_out = "C:\\桌面文件\\代码_数据\\data11years\\jq\\jq_filter2\\jq_splitByField\\"
for field, jq_afId_name_set in jq_field_jqAfidName.items():
    path_ = jq_out + field[0] + "_" + field[1] + "_" + "affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
    with open(path_, 'w', encoding='utf-8') as fout:
        with open(path5, 'r', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip('\n').split('\t')
                if (line[0], line[1]) in jq_afId_name_set:
                    fout.write('\t'.join(line)+'\n')
    path__ = jq_out + field[0] + "_" + field[1] + "_" + "affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt"
    with open(path__, 'w', encoding='utf-8') as fout:
        with open(path6, 'r', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip('\n').split('\t')
                if (line[0], line[1]) in jq_afId_name_set:
                    fout.write('\t'.join(line)+'\n')
# git test
