# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
去掉
pathOut = r"E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear(JQ_Co).txt"
中，包含杰青id的数据
"""
import pandas as pd

path = "/home/fengxu/桌面/RJ_experimentation_1/Data/result/dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_" \
       "paperID_authorID_affiliationID_paperYear_normalizedName_sortedName_displayName_chineseName_" \
       "awardYear_citationCnt.txt"

data = pd.read_csv(path, sep='\t', header=None,usecols=[1])
data = data.drop_duplicates()
pathOut = "/home/fengxu/桌面/RJ_experimentation_1/Data/compareGroupData/Jieqing_authorID.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)