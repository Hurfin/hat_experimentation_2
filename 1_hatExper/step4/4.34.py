# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
jq的数据在r"E:\pythonCode\RJ_experimentation_1\Data_1\new\1"

r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthor)fxID_jif11Years.txt"
r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthor)fxID_PaperCnt11Years.txt"
r"E:\FengXu\result1\fxID_assumeAwardYear_minYear_aveCitationCnt11years.txt"    （除以论文数，程序为4.33）
r"E:\FengXu\result1\(coAuthor)fxID_hIndex11years.txt"

将它们合并
"""
import pandas as pd

path1 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthor)" \
        r"fxID_hindex11years.txt"
path2 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthor)" \
        r"fxID_jif11Years.txt"
path3 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\(coAuthor)" \
        r"fxID_PaperCnt11Years.txt"
path4 = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author(affID_sortedName)\4\fxID_assumeAwardYear_" \
        r"minYear_aveCitationCnt11years(chuYiLunWenShu).txt"
y = ['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']
name1 = ['fxID'] + y
name2 = ['fxID'] + y
name3 = ['fxID'] + y
name4 = ['fxID', 'assumeAwardYear', 'minYear'] + y
data1 = pd.read_csv(path1, sep='\t', header=None, names=name1)
data2 = pd.read_csv(path2, sep='\t', header=None, names=name2)
data3 = pd.read_csv(path3, sep='\t', header=None, names=name3)
data4 = pd.read_csv(path4, sep='\t', header=None, names=name4)

data1['bf_hindex'] = data1.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data1['af_hindex'] = data1.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data1 = data1.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data2['bf_jif'] = data2.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data2['af_jif'] = data2.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data2 = data2.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data3['bf_paperCnt'] = data3.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data3['af_paperCnt'] = data3.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data3 = data3.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data4['bf_aveCitation'] = data4.apply(lambda x: (x['-5']+x['-4']+x['-3']+x['-2']+x['-1'])/5, axis=1)
data4['af_aveCitation'] = data4.apply(lambda x: (x['5']+x['4']+x['3']+x['2']+x['1'])/5, axis=1)
data4 = data4.drop(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'], axis=1)

data = pd.merge(data1, data2, on=['fxID'], how='left')
data = pd.merge(data, data3, on=['fxID'], how='left')
data = pd.merge(data, data4, on=['fxID'], how='left')
del data1, data2, data3, data4
data = data[['fxID', 'assumeAwardYear', 'minYear',
             'bf_jif', 'bf_aveCitation', 'bf_hindex', 'bf_paperCnt',
             'af_jif', 'af_aveCitation', 'af_hindex', 'af_paperCnt'
             ]]
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\co-authorData\co_author" \
           r"(affID_sortedName)\4\(coAuthorCombined)\(coAuthor)" + '_'.join(
            ['fxID', 'assumeAwardYear', 'minYear',
             'bf_jif', 'bf_aveCitation', 'bf_hindex', 'bf_paperCnt',
             'af_jif', 'af_aveCitation', 'af_hindex', 'af_paperCnt'
             ]) + "(chuYiLunWenShu).txt"
data.to_csv(path_out, sep='\t', index=False)
