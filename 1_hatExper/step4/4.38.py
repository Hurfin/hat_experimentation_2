# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author
(affID_sortedName)\1\fxID_affID_sortedName_coAuthorID_coAuthorPaperMinYear_coAuthorPaperMaxYear.txt
"E:\FengXu\result1\jqPaperID_authorID_affID.txt"
算杰青获奖前后的合作者数量
# "E:\FengXu\result2\jqPaperID_coAuthorID_affID_normalizedName.txt"
"""
import pandas as pd


def getCo(paperID_list):
    # input 杰青的paperID列表
    # return coAuthor的数量
    paperID_list = list(map(str, paperID_list))
    paperID_list = set(paperID_list)
    # print('fuck1', len(paperID_list))
    # path = r"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\jqPaperID_coAuthorID_affID_normalizedName.txt"
    path = r"E:\FengXu\result2\jqPaperID_coAuthorID_affID_normalizedName.txt"
    affID_normalizedName_index_dict = dict()
    coAuthorID_index_dict = dict()
    cnt = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            if line[0] in paperID_list:  # 如果是在该jq的paper列表里
                # print("OK1")
                # print(line)
                if (line[2], line[3]) not in affID_normalizedName_index_dict.keys():  # 如果(affID_normalizedName)没有记录的话
                    if line[1] in coAuthorID_index_dict.keys():  # 那就看coAuthor里有没有被记录过
                        # 如果记录过的话就把coAuthor对应的编号给它
                        affID_normalizedName_index_dict[(line[2], line[3])] = coAuthorID_index_dict[line[1]]
                    else:  # 如果coAuthor里没有记录过的话
                        affID_normalizedName_index_dict[(line[2], line[3])] = cnt
                        coAuthorID_index_dict[line[1]] = cnt
                        cnt += 1
                else:  # 如果(affID_normalizedName)已经有记录了
                    coAuthorID_index_dict[line[1]] = affID_normalizedName_index_dict[(line[2], line[3])]
                pass
        pass
    return cnt
    pass


# path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\JQ_" \
#         r"affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
# path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\_tmpSave\jqPaperID_coAuthorID_affID_normalizedName.txt"
path1 = r"E:\FengXu\result2\JQ_" \
        r"affiliationID_sortedName_fieldID_fieldName_paperID_authorID_paperYear_awardYear_citationCnt.txt"
path2 = r"E:\FengXu\result2\jqPaperID_coAuthorID_affID_normalizedName.txt"

# affID	sortedName	fieldID	fieldName	paperID	authorID	paperYear	awardYear	citationCnt
data1 = pd.read_csv(path1, sep='\t')  # 需要的杰青的full data
# data2 = pd.read_csv(path2, se='\t', header=None, names=['jqPaperID', 'coAuthorID', 'affID', 'normalizedName'])

# fout = open(r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\affID_sortedName_awardYear_"
#             r"coAuthorsNumBF_coAuthorsNumAF.txt", 'w', encoding='utf-8')
fout = open(r"E:\FengXu\result2\affID_sortedName_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt",
            'w', encoding='utf-8')
fout.write("affID\tsortedName\tawardYear\tcoAuthorsNumBF\tcoAuthorsNumAF\n")
data1 = data1.groupby(['affID', 'sortedName', 'awardYear'])
for k, group in data1:
    affID_i = k[0]
    sortedName_i = k[1]
    awardYear_i = k[2]
    # 该杰青前5年的论文id
    PIDs_bf = list(group[(-5 <= (group['paperYear'] - awardYear_i)) & ((group['paperYear'] - awardYear_i) <= -1)]['paperID'])
    # 后五年论文
    PIDs_af = list(group[(1 <= (group['paperYear'] - awardYear_i)) & ((group['paperYear'] - awardYear_i) <= 5)]['paperID'])

    # print(len(PIDs_bf), len(PIDs_af))
    # print(PIDs_bf, PIDs_af)

    coAuthorNumsBf = getCo(PIDs_bf)
    coAuthorNumsAf = getCo(PIDs_af)
    # print(coAuthorNumsBf, coAuthorNumsAf)
    # print("_______")
    fout.write(str(affID_i)+'\t'+str(sortedName_i)+'\t'+str(awardYear_i)+'\t'
               +str(coAuthorNumsBf)+'\t'+str(coAuthorNumsAf)+'\n')
    pass
fout.close()

