# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
对照组合并到一起
杰青组合并到一起
杰青组
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveCitationCntPerYear(before5ANDafter5).txt
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveJIFPerYear(before5ANDafter5).txt
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_h-IndexPerYear(before5ANDafter5).txt
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_paperCntPerYear(Before5ANDafter5).txt
对照组
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_aveCitationPerYear(Before5ANDafter5).txt
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_aveJIFPerYear(Before5ANDafter5).txt
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_h-indexPerYear(Before5ANDafter5).txt
E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_paperCntPerYear(Before5ANDafter5).txt
对应关系
E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\coAuthor\selectedCoAuthor\ans_JQ_map_coAuthor.txt
"""
import numpy as np
import pandas as pd
path1 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
        r"aveCitationCntPerYear(before5ANDafter5).txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
        r"aveJIFPerYear(before5ANDafter5).txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
        r"h-IndexPerYear(before5ANDafter5).txt"
path4 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_" \
        r"paperCntPerYear(Before5ANDafter5).txt"

names1 = ['affiliationID', 'sortedName', 'k1', 'b1', 'k2', 'b2', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']
data1 = pd.read_csv(path1, sep='\t', header=None, names=names1)
data1['aveCitationCnt'] = data1.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data1 = data1[['affiliationID', 'sortedName', 'aveCitationCnt']]

data2 = pd.read_csv(path2, sep='\t', header=None, names=names1)
data2['aveJIF'] = data2.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data2 = data2[['affiliationID', 'sortedName', 'aveJIF']]

data3 = pd.read_csv(path3, sep='\t', header=None, names=names1)
data3['aveH-Index'] = data3.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data3 = data3[['affiliationID', 'sortedName', 'aveH-Index']]

data4 = pd.read_csv(path4, sep='\t', header=None, names=names1)
data4['avePaperCnt'] = data4.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data4 = data4[['affiliationID', 'sortedName', 'avePaperCnt']]


# data = data1.merge(data2, on=['affiliationID', 'sortedName'], how='inner')
# data = data.merge(data3, on=['affiliationID', 'sortedName'], how='inner')
# data = data.merge(data4, on=['affiliationID', 'sortedName'], how='inner')

data = data1.merge(data2, on=['affiliationID', 'sortedName'], how='outer')
data = data.merge(data3, on=['affiliationID', 'sortedName'], how='outer')
data = data.merge(data4, on=['affiliationID', 'sortedName'], how='outer')
selectCols = ['affiliationID', 'sortedName', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt']
data = data[selectCols]
data = data.fillna(0)
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_affiliationID_sortedName_" \
          r"aveCitationCnt_aveJIF_aveH-Index_avePaperCnt.txt"
data.to_csv(pathOut, sep='\t', header=None, index=False)



path5 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_"\
        r"aveCitationPerYear(Before5ANDafter5).txt"
path6 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_"\
        r"aveJIFPerYear(Before5ANDafter5).txt"
path7 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_"\
        r"h-indexPerYear(Before5ANDafter5).txt"
path8 = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result_DZ\DZ_authorID_assumeAwardYear_k1_b1_k2_b2_"\
        r"paperCntPerYear(Before5ANDafter5).txt"
names2 = ['DZ_authorID', 'assumeAwardYear', 'k1', 'b1', 'k2', 'b2', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']

data1 = pd.read_csv(path5, sep='\t', header=None, names=names2)
data2 = pd.read_csv(path6, sep='\t', header=None, names=names2)
data3 = pd.read_csv(path7, sep='\t', header=None, names=names2)
data4 = pd.read_csv(path8, sep='\t', header=None, names=names2)

data1['aveCitationCnt'] = data1.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data1 = data1[['DZ_authorID', 'assumeAwardYear', 'aveCitationCnt']]

data2['aveJIF'] = data2.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data2 = data2[['DZ_authorID', 'assumeAwardYear', 'aveJIF']]

data3['aveH-Index'] = data3.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data3 = data3[['DZ_authorID', 'assumeAwardYear', 'aveH-Index']]

data4['avePaperCnt'] = data4.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)  # 将每行的获奖前五年的值相加除5
data4 = data4[['DZ_authorID', 'assumeAwardYear', 'avePaperCnt']]


# data = data1.merge(data2, on=['DZ_authorID', 'assumeAwardYear'], how='inner')
# data = data.merge(data3, on=['DZ_authorID', 'assumeAwardYear'], how='inner')
# data = data.merge(data4, on=['DZ_authorID', 'assumeAwardYear'], how='inner')
data = data1.merge(data2, on=['DZ_authorID', 'assumeAwardYear'], how='outer')
data = data.merge(data3, on=['DZ_authorID', 'assumeAwardYear'], how='outer')
data = data.merge(data4, on=['DZ_authorID', 'assumeAwardYear'], how='outer')
selectCols2 = ['DZ_authorID', 'assumeAwardYear', 'aveCitationCnt', 'aveJIF', 'aveH-Index', 'avePaperCnt']
data = data[selectCols2]
data = data.fillna(0)
pathOut2 = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\DZ_authorID_assumeAwardYear_" \
           r"aveCitationCnt_aveJIF_aveH-Index_avePaperCnt.txt"
data.to_csv(pathOut2, sep='\t', header=None, index=False)
