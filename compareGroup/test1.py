# -*- coding: utf-8 -*-
# !/usr/bin/env python
# import pandas as pd
#
# path = r"E:\pythonCode\RJ_experimentation_1\Data\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
#        r"paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
#        r"awardYear_citationCnt.txt"
#
# data = pd.read_csv(path, sep='\t', header=None, usecols=[0])
#
# data = data.drop_duplicates()
#
# pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\Jieqing_paperIDs.txt"
# data.to_csv(pathOut, sep='\t', header=None, index=False)

import pandas as pd
Jieqing_paperIDs_SET = set()
path1 = r"E:\FengXu\result\compareGroupData\tmp\Jieqing_paperIDs.txt"
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        Jieqing_paperIDs_SET.add(line[0])
    pass

path2 = r"D:\Dataset\NEW_MAG\Papers.txt"
ucols = [0, 7]
papers = pd.read_csv(path2, sep='\t', header=None, usecols=ucols, names=['paperID', 'paperYear'])
papers = papers.drop_duplicates()

pathOut = r"E:\FengXu\result\compareGroupData\Jieqing_paperID_year"
fout = open(pathOut, 'w', encoding='utf-8')
for i in range(0, len(papers)):
    paperid = papers.iloc[i]['paperID']
    year = papers.iloc[i]['paperYear']
    if paperid in Jieqing_paperIDs_SET:
        fout.write(str(paperid)+'\t'+str(year)+'\n')
    pass
fout.close()
