# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""

"""
import pandas as pd
# # dz1.txt
# # fxID	fieldID	fieldName	assumeAwardYear	minYear	bf_jif	bf_citation	bf_hindex	bf_papercnt
# # L	M	H	af_jif	af_citation	af_hindex	af_papercnt
# # 需要把不除以论文数的citation给放上（bf_citationBuChu, af_citationBuChu）
#
# # jq1.txt
# # affID	sortedName	awardYear	fieldID	fieldName	bf_jif	bf_citation	bf_hindex	bf_papercnt
# # L	M	H	af_jif	af_citation	af_hindex	af_papercnt
# # 需要把不除以论文数的citation给放上（bf_citationBuChu, af_citationBuChu）
# path1 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt"
# path2 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_LMH_assumeAwardYear_minYear_aveCitationCnt11years(buChuYiLunWenShu).txt"
#
# affID	sortedName	awardYear	fieldID	fieldName	bf_jif	bf_citation	bf_hindex	bf_papercnt	L	M	H	af_jif	af_citation	af_hindex	af_papercnt
path3 = r"C:\Users\12433\Desktop\data11years\field\jq.txt"
# fxID	fieldID	fieldName	assumeAwardYear	minYear	bf_jif	bf_citation	bf_hindex	bf_papercnt	L	M	H	af_jif	af_citation	af_hindex	af_papercnt
path4 = r"C:\Users\12433\Desktop\data11years\field\dz.txt"
#
# names1 = ['affID', 'sortedName', 'L', 'M', 'H', 'fieldID', 'fieldName', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
#           'c9', 'c10', 'c11']
# names2 = ['fxID', 'L', 'M', 'H', 'assumeAwardYear', 'minYear', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
#           'c9', 'c10', 'c11']
# jqCitationData = pd.read_csv(path1, sep='\t', header=None, names=names1)
# dzCitationData = pd.read_csv(path2, sep='\t', header=None, names=names2)
#
# jqCitationData['bf_citationBuChu'] = jqCitationData.apply(lambda x: (x['c1']+x['c2']+x['c3']+x['c4']+x['c5'])/5, axis=1)
# jqCitationData['af_citationBuChu'] = jqCitationData.apply(lambda x: (x['c7']+x['c8']+x['c9']+x['c10']+x['c11'])/5, axis=1)
# jqCitationData = jqCitationData[['affID', 'sortedName', 'bf_citationBuChu', 'af_citationBuChu']]
# jqCitationData.to_csv(r"C:\Users\12433\Desktop\data11years\field\jqCitationData(buChu).txt", sep='\t', index=False)
#
# dzCitationData['bf_citationBuChu'] = dzCitationData.apply(lambda x: (x['c1']+x['c2']+x['c3']+x['c4']+x['c5'])/5, axis=1)
# dzCitationData['af_citationBuChu'] = dzCitationData.apply(lambda x: (x['c7']+x['c8']+x['c9']+x['c10']+x['c11'])/5, axis=1)
# dzCitationData = dzCitationData[['fxID', 'bf_citationBuChu', 'af_citationBuChu']]
# dzCitationData.to_csv(r"C:\Users\12433\Desktop\data11years\field\dzCitationData(buChu).txt", sep='\t', index=False)


# dz = pd.read_csv(path4, sep='\t')
# jq = pd.read_csv(path3, sep='\t')
# path1 = r"C:\Users\12433\Desktop\data11years\field\dzCitationData(buChu).txt"
# path2 = r"C:\Users\12433\Desktop\data11years\field\jqCitationData(buChu).txt"
# dzCitationData = pd.read_csv(path1, sep='\t')
# jqCitationData = pd.read_csv(path2, sep='\t')
#
# print(list(dz.columns), '\n', list(jq.columns))
# print(list(dzCitationData.columns), list(jqCitationData.columns))
# dz = dz.merge(dzCitationData, on=['fxID'], how='inner')
# jq = jq.merge(jqCitationData, on=['affID', 'sortedName'], how='inner')
# print(dz.shape[0], jq.shape[0])
#
# dzOrder = ['fxID', 'fieldID', 'fieldName', 'assumeAwardYear', 'minYear', 'bf_jif', 'bf_citation', 'bf_hindex', 'bf_papercnt', 'bf_citationBuChu',
#            'L', 'M', 'H', 'af_jif', 'af_citation', 'af_hindex', 'af_papercnt', 'af_citationBuChu']
# dz = dz[dzOrder]
#
# jqOrder = ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName', 'bf_jif', 'bf_citation', 'bf_hindex', 'bf_papercnt', 'bf_citationBuChu',
#            'L', 'M', 'H', 'af_jif', 'af_citation', 'af_hindex', 'af_papercnt', 'af_citationBuChu']
# jq = jq[jqOrder]
# jq.to_csv(r"C:\Users\12433\Desktop\data11years\field\jqFull.txt", sep='\t', index=False)
# dz.to_csv(r"C:\Users\12433\Desktop\data11years\field\dzFull.txt", sep='\t', index=False)
#

# affID	sortedName	awardYear	fieldID	fieldName	bf_jif	bf_citation	bf_hindex	bf_papercnt	bf_citationBuChu
# L	M	H	af_jif	af_citation	af_hindex	af_papercnt	af_citationBuChu
path1 = r"C:\Users\12433\Desktop\data11years\field\jqFull.txt"
# fxID	fieldID	fieldName	assumeAwardYear	minYear	bf_jif	bf_citation	bf_hindex	bf_papercnt	bf_citationBuChu
# L	M	H	af_jif	af_citation	af_hindex	af_papercnt	af_citationBuChu
path2 = r"C:\Users\12433\Desktop\data11years\field\dzFull.txt"

# 杰青获奖前后的合作密度和合作者数量
path3 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt"
path4 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"

path5 = r"C:\Users\12433\Desktop\data11years\dz\filter1\dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt"
path6 = r"C:\Users\12433\Desktop\data11years\dz\filter1\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"

dzFull = pd.read_csv(path2, sep='\t')
jqFull = pd.read_csv(path1, sep='\t')

jqCII = pd.read_csv(path3, sep='\t')
jqCoAuthorNum = pd.read_csv(path4, sep='\t')
jqCII = jqCII.drop(['L', 'M', 'H'], axis=1)
jqCoAuthorNum = jqCoAuthorNum.drop(['L', 'M', 'H', 'awardYear'], axis=1)

dzCII = pd.read_csv(path5, sep='\t')
dzCoAuthorNum = pd.read_csv(path6, sep='\t')
dzCII = dzCII.drop(['L', 'M', 'H', 'assumeAwardYear'], axis=1)
dzCoAuthorNum = dzCoAuthorNum.drop(['L', 'M', 'H', 'dzAwardYear'], axis=1)

dzFull = pd.merge(dzFull, dzCII, left_on=['fxID'], right_on=['dzFxID'], how='inner')
dzFull = dzFull.drop(['dzFxID'], axis=1)
dzFull = pd.merge(dzFull, dzCoAuthorNum, left_on=['fxID'], right_on=['dzFxID'], how='inner')
dzFull = dzFull.drop(['dzFxID'], axis=1)
dzOrder = ['fxID', 'fieldID', 'fieldName', 'assumeAwardYear', 'minYear', 'bf_jif', 'bf_citation', 'bf_hindex', 'bf_papercnt',
           'bf_citationBuChu', 'aveCIIBF', 'dzCoAuthorsNumBF',
            'L', 'M', 'H', 'af_jif', 'af_citation', 'af_hindex', 'af_papercnt', 'af_citationBuChu', 'aveCIIAF', 'dzCoAuthorsNumAF']
dzFull = dzFull[dzOrder]
dzFull.to_csv(r"C:\Users\12433\Desktop\data11years\field\dzFull_new.txt", sep='\t', index=False)

jqFull = pd.merge(jqFull, jqCII, on=['affID', 'sortedName'], how='inner')
jqFull = pd.merge(jqFull, jqCoAuthorNum, on=['affID', 'sortedName'], how='inner')
jqOrder = ['affID', 'sortedName', 'awardYear', 'fieldID', 'fieldName', 'bf_jif', 'bf_citation', 'bf_hindex',
           'bf_papercnt', 'bf_citationBuChu', 'aveCIIBF', 'coAuthorsNumBF',
            'L', 'M', 'H', 'af_jif', 'af_citation', 'af_hindex', 'af_papercnt', 'af_citationBuChu', 'aveCIIAF', 'coAuthorsNumAF']
jqFull = jqFull[jqOrder]
jqFull.to_csv(r"C:\Users\12433\Desktop\data11years\field\jqFull_new.txt", sep='\t', index=False)
