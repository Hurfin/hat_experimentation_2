# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"
r"E:\FengXu\tmp\dz_" \
        r"fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
找对照组的前后合作密度（以及前后的合作者数量变化）

先求前后合作者数量变化，这个应该比较好求点
"""
import pandas as pd


def getCo(paperID_list):
    # input dz的paperID列表
    # return dz的coAuthor的数量
    paperID_list = list(map(str, paperID_list))
    paperID_list = set(paperID_list)

    # path = r"E:\FengXu\result2\jqPaperID_coAuthorID_affID_normalizedName.txt"
    path = r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"
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

path0 = r"E:\FengXu\tmp\dz_" \
        r"fxID_coAuthorID_coAuthorPaperID_coAuthorPaperYear_journalID_minYear_maxYear_assumeAwardYear.txt"
path1 = r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"

data1 = pd.read_csv(path0, sep='\t', header=None,
                    names=['fxID', 'coAuthorID', 'coAuthorPaperID', 'coAuthorPaperYear', 'journalID', 'minYear',
                           'maxYear', 'assumeAwardYear'])
data1 = data1.astype({'fxID': str, 'coAuthorID': str, 'coAuthorPaperID': str, 'coAuthorPaperYear': int,
                      'journalID': str, 'minYear': int, 'maxYear': int, 'assumeAwardYear': int})
data1 = data1.groupby(['fxID', 'assumeAwardYear'])

fout = open(r"E:\FengXu\result3\dzFxID_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt", 'w', encoding='utf-8')
fout.write("dzFxID\tdzAwardYear\tdzCoAuthorsNumBF\tdzCoAuthorsNumAF\n")
for k, group in data1:
    fxID_i = k[0]
    assumeAwardYear_i = k[1]
    PIDs_BF = list(group[(group['coAuthorPaperYear'] - assumeAwardYear_i >= -5) &
                         (group['coAuthorPaperYear'] - assumeAwardYear_i <= -1)]['coAuthorPaperID'])
    PIDs_AF = list(group[(group['coAuthorPaperYear'] - assumeAwardYear_i >= 1) &
                         (group['coAuthorPaperYear'] - assumeAwardYear_i <= 5)]['coAuthorPaperID'])
    # 5 before num
    NumBF = getCo(PIDs_BF)
    # 5 after num
    NumAF = getCo(PIDs_AF)
    fout.write(fxID_i+'\t'+str(assumeAwardYear_i)+'\t'+str(NumBF)+'\t'+str(NumAF)+'\n')
    pass
fout.close()
