# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
path="E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear_firstPaperYear(Co).txt"

筛选在
"""
import pandas as pd

path2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\paperID_authorID_affiliationID" \
        r"_paperYear_firstPaperYear(Co).txt"
names2 = ['paperID', 'authorID', 'affiliationID', 'paperYear', 'firstPaperYear']
data2 = pd.read_csv(path2, sep='\t', header=None, names=names2)

coAuthorID_firstPaperYear = data2[['authorID', 'firstPaperYear']]
coAuthorID_firstPaperYear = coAuthorID_firstPaperYear.drop_duplicates()

coAuthorID_list = []  # 学术年龄符合条件的(age在5-25之间的)
coAuthorID_APPEND = coAuthorID_list.append
for i in range(0, len(coAuthorID_firstPaperYear)):
    authorID = coAuthorID_firstPaperYear.iloc[i]['authorID']
    firstPaperYear = coAuthorID_firstPaperYear.iloc[i]['firstPaperYear']
    for year in range(1994, 2016):
        if (year - firstPaperYear >= 5) and (year - firstPaperYear <= 25):
            coAuthorID_APPEND(authorID)
            break
            pass
# print(len(coAuthorID_list))
# 149198
coAuthorID_age = pd.DataFrame({'authorID': coAuthorID_list})

path3 = r"E:\pythonCode\RJ_experimentation_1\Data\CN_affiliations\CN_affiliations.txt"
CN_affiliationID = pd.read_csv(path3, sep='\t', header=None, usecols=[1], names=['affiliationID'])
data_x = data2.merge(CN_affiliationID, on=['affiliationID'], how='inner')
data_x = data_x[['authorID']]
data_x = data_x.drop_duplicates()
# data_x 机构国家满足条件的(CN)

authorID_paperCnt = data2.groupby('authorID')['paperID'].count()
authorID_paperCnt = authorID_paperCnt.reset_index()
authorID_paperCnt.columns = ['authorID', 'paperCnt']
authorID_paperCnt = authorID_paperCnt[authorID_paperCnt['paperCnt'] > 5]
authorID_pCnt = authorID_paperCnt[['authorID']]
authorID_pCnt = authorID_pCnt.drop_duplicates()
# authorID_pCnt 论文数大于5篇的


tmp = coAuthorID_age.merge(data_x, how='inner')
tmp = tmp.merge(authorID_pCnt, how='inner')
tmp = tmp[['authorID']]
print(tmp.shape[0])
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\coAuthor_age5_25_Aff_CN_paperNum5more.txt"
tmp.to_csv(pathOut, sep='\t', header=None, index=False)
