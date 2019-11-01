# -*- coding: utf-8 -*-
# !/usr/bin/env python

# path1 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_JIF(11years).txt"
# path2 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sorteName_fieldID_fieldName_aveCitation(11years).txt"
#
# jq_set = set()
# with open(path2, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         jq_set.add((line[0], line[1]))
#         pass
#     pass
#
# jq__ = list()
# jq_set1 = set()
# with open(path1, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         jq_set1.add((line[0], line[1]))
#         jq__.append(line)
#         pass
#     pass
#
# print(list(jq_set - jq_set1))
# xx = list(jq_set - jq_set1)
# print(list(map(str, [0 for i in range(1, 12)])))
# vv = list(map(str, [0 for i in range(1, 12)]))
# with open(path1, 'w', encoding='utf-8') as f:
#     for line in jq__:
#         f.write('\t'.join(line)+'\n')
#     f.write(xx[0][0]+'\t'+xx[0][1]+'\t'+'\t'.join(vv)+'\n')
#     pass
#


"""
9个领域：
1.每个领域前后五年的平均 Paper，JIF，Citation，H-index 对照+杰青
2.每个领域前后五年的平均 CII，Coauthor 对照+杰青

fieldID, fieldName, jq, bf(5 parameters ave), af(5 parameters ave)
fieldID, fieldName, dz, bf(5 parameters ave), af(5 parameters ave)

"""
getFields_jq = set()
getFields_dz = set()
path1 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_fieldID_fieldName.txt"
path2 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sorteName_LMH_" \
        r"fieldID_fieldName_aveCitation(11years).txt"
# 含有领域的信息，能帮助找到有多少个领域
jqFields_cnt = dict()
dzFields_cnt = dict()

with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        getFields_dz.add((line[1], line[2]))
        if (line[1], line[2]) not in dzFields_cnt.keys():
            dzFields_cnt[(line[1], line[2])] = 0
        dzFields_cnt[(line[1], line[2])] += 1
    pass

with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        getFields_jq.add((line[5], line[6]))
        if (line[5], line[6]) not in jqFields_cnt.keys():
            jqFields_cnt[(line[5], line[6])] = 0
        jqFields_cnt[(line[5], line[6])] += 1
    pass
dzFields_CNT_list = list()
jqFields_CNT_list = list()
print("dz")
for k, v in dzFields_cnt.items():
    print(k, v)
    dzFields_CNT_list.append([k, v])
print("jq")
for k, v in jqFields_cnt.items():
    print(k, v)
    jqFields_CNT_list.append([k, v])

import pandas as pd
# fxID	fieldID	fieldName	assumeAwardYear	minYear	bf_jif	bf_citation	bf_hindex	bf_papercnt	bf_citationBuChu
# aveCIIBF	dzCoAuthorsNumBF	 L	M	H	af_jif	af_citation	af_hindex	af_papercnt	af_citationBuChu	aveCIIAF	dzCoAuthorsNumAF
dzFull_new = pd.read_csv(r"C:\Users\12433\Desktop\data11years\field\dzFull_new.txt", sep='\t')
# affID	sortedName	awardYear	fieldID	fieldName	bf_jif	bf_citation	bf_hindex	bf_papercnt	bf_citationBuChu
# aveCIIBF	coAuthorsNumBF	L	M	H	af_jif	af_citation	af_hindex	af_papercnt	af_citationBuChu	aveCIIAF	coAuthorsNumAF
jqFull_new = pd.read_csv(r"C:\Users\12433\Desktop\data11years\field\jqFull_new.txt", sep='\t')

dzFull_new = dzFull_new.groupby(['fieldID', 'fieldName'])
jqFull_new = jqFull_new.groupby(['fieldID', 'fieldName'])
outerdz = open(r"C:\Users\12433\Desktop\data11years\field\dz_fields.txt", 'w', encoding='utf-8')
outerjq = open(r"C:\Users\12433\Desktop\data11years\field\jq_fields.txt", 'w', encoding='utf-8')
# dz按领域分组后循环每个领域
outerdz.write("fieldID\tfieldName\tpeopleNums\tjifBF\tjifAF\thindexBF\thindexAF\tpaperCntBF\tpaperCntAF\t"
              "citationBF\tcitationAF\tcitationBuChuBF\tcitationBuChuAF\tCIIBF\tCIIAF\tcoAuthorNumBF\tcoAuthorNumAF\n")
for fieldID_fieldName, group in dzFull_new:
    # jif hindex paperCnt citation citationBuChu CII coAuthorNum
    fieldID = fieldID_fieldName[0]
    fieldName = fieldID_fieldName[1]

    jifBF = list(group['bf_jif'])
    jifAF = list(group['af_jif'])

    hindexBF = list(group['bf_hindex'])
    hindexAF = list(group['af_hindex'])

    paperCntBF = list(group['bf_papercnt'])
    paperCntAF = list(group['af_papercnt'])

    citationBF = list(group['bf_citation'])
    citationAF = list(group['af_citation'])

    citationBuChuBF = list(group['bf_citationBuChu'])
    citationBuChuAF = list(group['af_citationBuChu'])

    CIIBF = list(group['aveCIIBF'])
    CIIAF = list(group['aveCIIAF'])

    coAuthorsNumBF = list(group['dzCoAuthorsNumBF'])
    coAuthorsNumAF = list(group['dzCoAuthorsNumAF'])

    xx = [str(fieldID), fieldName, str(dzFields_cnt[(str(fieldID), fieldName)]),
          str(sum(jifBF)/len(jifBF)), str(sum(jifAF)/len(jifAF)),
          str(sum(hindexBF)/len(hindexBF)), str(sum(hindexAF)/len(hindexAF)),
          str(sum(paperCntBF)/len(paperCntBF)), str(sum(paperCntAF)/len(paperCntAF)),
          str(sum(citationBF)/len(citationBF)), str(sum(citationAF)/len(citationAF)),
          str(sum(citationBuChuBF) / len(citationBuChuBF)), str(sum(citationBuChuAF) / len(citationBuChuAF)),
          str(sum(CIIBF)/len(CIIBF)), str(sum(CIIAF)/len(CIIAF)),
          str(sum(coAuthorsNumBF)/len(coAuthorsNumBF)), str(sum(coAuthorsNumAF)/len(coAuthorsNumAF))
          ]
    outerdz.write('\t'.join(xx)+'\n')
    pass
outerdz.close()



# affID	sortedName	awardYear	fieldID	fieldName	bf_jif	bf_citation	bf_hindex	bf_papercnt	bf_citationBuChu
# aveCIIBF	coAuthorsNumBF	L	M	H	af_jif	af_citation	af_hindex	af_papercnt	af_citationBuChu	aveCIIAF	coAuthorsNumAF
# jq按领域分组后循环每个领域
outerjq.write("fieldID\tfieldName\tpeopleNums\tjifBF\tjifAF\thindexBF\thindexAF\tpaperCntBF\tpaperCntAF\t"
              "citationBF\tcitationAF\tcitationBuChuBF\tcitationBuChuAF\tCIIBF\tCIIAF\tcoAuthorNumBF\tcoAuthorNumAF\n")
for fieldID_fieldName, group in jqFull_new:
    # jif hindex paperCnt citation citationBuChu CII coAuthorNum
    fieldID = fieldID_fieldName[0]
    fieldName = fieldID_fieldName[1]

    jifBF = list(group['bf_jif'])
    jifAF = list(group['af_jif'])

    hindexBF = list(group['bf_hindex'])
    hindexAF = list(group['af_hindex'])

    paperCntBF = list(group['bf_papercnt'])
    paperCntAF = list(group['af_papercnt'])

    citationBF = list(group['bf_citation'])
    citationAF = list(group['af_citation'])

    citationBuChuBF = list(group['bf_citationBuChu'])
    citationBuChuAF = list(group['af_citationBuChu'])

    CIIBF = list(group['aveCIIBF'])
    CIIAF = list(group['aveCIIAF'])

    coAuthorsNumBF = list(group['coAuthorsNumBF'])
    coAuthorsNumAF = list(group['coAuthorsNumAF'])

    xx = [str(fieldID), fieldName, str(jqFields_cnt[(str(fieldID), fieldName)]),
          str(sum(jifBF) / len(jifBF)), str(sum(jifAF) / len(jifAF)),
          str(sum(hindexBF) / len(hindexBF)), str(sum(hindexAF) / len(hindexAF)),
          str(sum(paperCntBF) / len(paperCntBF)), str(sum(paperCntAF) / len(paperCntAF)),
          str(sum(citationBF) / len(citationBF)), str(sum(citationAF) / len(citationAF)),
          str(sum(citationBuChuBF) / len(citationBuChuBF)), str(sum(citationBuChuAF) / len(citationBuChuAF)),
          str(sum(CIIBF) / len(CIIBF)), str(sum(CIIAF) / len(CIIAF)),
          str(sum(coAuthorsNumBF) / len(coAuthorsNumBF)), str(sum(coAuthorsNumAF) / len(coAuthorsNumAF))
          ]
    outerjq.write('\t'.join(xx) + '\n')
    pass

outerjq.close()
