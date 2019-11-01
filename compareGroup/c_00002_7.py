# -*- coding: utf-8 -*-
# !/usr/bin/env python
import numpy as np
import pandas as pd

# path1 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
# path2 = r"E:\FengXu\result\compareGroupData\DZ_paperID.txt"
# # path3 = r"E:\pythonCode\RJ_experimentation_1\Data\result\JIFfrom1989to2017_MAG_" \
# #         r"JieqingContributeJournal\journalID_JIF_perYear_from1989to2017.txt"
#
# data1 = pd.read_csv(path1, sep='\t', header=None, names=['paperID', 'year', 'journalID'])
# data2 = pd.read_csv(path2, sep='\t', header=None, names=['paperID'])
# data = pd.merge(data1, data2, on=['paperID'], how='inner')
# del data1, data2
# data = data[['paperID', 'journalID']]
# pathOut1 = r"E:\FengXu\result\compareGroupData\DZ_data\DZ_paperID_journalID.txt"
# data.to_csv(pathOut1, sep='\t', header=None, index=False)
#
# data1 = data[['journalID']]
# data1 = data1.drop_duplicates()
# pathOut2 = r"E:\FengXu\result\compareGroupData\DZ_data\journalID(DZ_need).txt"
# data1.to_csv(pathOut2, sep='\t', header=None, index=False)
#
# data2 = data[['paperID']]
# data2 = data2.drop_duplicates()
# pathOut3 = r"E:\FengXu\result\compareGroupData\DZ_data\paperID(DZ_hasJournalID).txt"
# data2.to_csv(pathOut3, sep='\t', header=None, index=False)

path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\JIFfrom1989to2017_MAG_" \
       r"JieqingContributeJournal\journalID_JIF_perYear_from1989to2017.txt"
path2 = r"C:\Users\12433\Desktop\Data\journalID(DZ_need).txt"

data1 = pd.read_csv(path1, sep='\t', header=None, usecols=[0], names=['journalID'])
data2 = pd.read_csv(path2, sep='\t', header=None, names=['DZ_journalID'])

set1 = set(list(data1['journalID']))  # 拥有JIF的journal id
set2 = set(list(data2['DZ_journalID']))  # 对照组需要JIF的journal id

print(len(set2-set1))
print(len(set1-set2))