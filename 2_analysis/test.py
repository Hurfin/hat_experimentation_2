# -*- coding: utf-8 -*-
# !/usr/bin/env python

path = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveJIFPerYear(before5ANDafter5).txt"
# path = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_h-IndexPerYear(before5ANDafter5).txt"
# path = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_paperCntPerYear(Before5ANDafter5).txt"
# path = r"E:\pythonCode\RJ_experimentation_1\Data\result\experment1_result\affiliationID_sortedName_k1_b1_k2_b2_aveCitationCntPerYear(before5ANDafter5).txt"
import pandas as pd

data = pd.read_csv(path, sep='\t', header=None, usecols=[0, 1, 2, 4])
data.columns = ['affiliationID', 'sortedName', 'k1', 'k2']

print(len(data))
print(data[data['k2']-data['k1']>0].shape[0])
print(data[data['k2']-data['k1']==0].shape[0])
print(data[data['k2']-data['k1']<0].shape[0])

"""
paperCnt
1393
535
116
742
aveCitation
1393
483
123
787
h-index
1393
461
151
781
aveJIF
1196
549
67
580
"""
