# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""

"""
import pandas as pd
# fxID	fieldID	fieldName	assumeAwardYear	minYear	bf_jif	bf_citation	bf_hindex
# bf_papercnt	L	M	H	af_jif	af_citation	af_hindex	af_papercnt
dzPath = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\dz.txt"
# affID	sortedName	awardYear	fieldID	fieldName	bf_jif	bf_citation	bf_hindex
# bf_papercnt	L	M	H	af_jif	af_citation	af_hindex	af_papercnt
jqPath = r"E:\pythonCode\RJ_experimentation_1\Data_1\1ans\jq.txt"

flag_ = True
jq_LMH_dict = dict()
with open(jqPath, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if flag_ is True:
            flag_ = False
            continue
        jq_LMH_dict[(line[0], line[1])] = [line[9], line[10], line[11]]
        pass
    pass

flag_ = True
dz_LMH_dict = dict()
with open(dzPath, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if flag_ is True:
            flag_ = False
            continue
        dz_LMH_dict[(line[0])] = [line[9], line[10], line[11]]
        pass
    pass


path1 = r"C:\Users\12433\Desktop\data11years\dz\filter\(coAuthor)fxID_hindex11years.txt"
path2 = r"C:\Users\12433\Desktop\data11years\dz\filter\(coAuthor)fxID_jif11Years.txt"
path3 = r"C:\Users\12433\Desktop\data11years\dz\filter\(coAuthor)fxID_PaperCnt11Years.txt"
path4 = r"C:\Users\12433\Desktop\data11years\dz\filter\fxID_" \
           r"assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt"
path5 = r"C:\Users\12433\Desktop\data11years\dz\filter\fxID_assumeAwardYear_minYear_" \
           r"aveCitationCnt11years(buChuYiLunWenShu).txt"

pathOut1 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_LMH_hindex11years.txt"
pathOut2 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_LMH_jif11Years.txt"
pathOut3 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_LMH_PaperCnt11Years.txt"
pathOut4 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_LMH_" \
           r"assumeAwardYear_minYear_aveCitationCnt11years(chuYiLunWenShu).txt"
pathOut5 = r"C:\Users\12433\Desktop\data11years\dz\filter1\fxID_LMH_assumeAwardYear_minYear_" \
           r"aveCitationCnt11years(buChuYiLunWenShu).txt"

fout = open(pathOut1, 'w', encoding='utf-8')
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut2, 'w', encoding='utf-8')
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut3, 'w', encoding='utf-8')
with open(path3, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut4, 'w', encoding='utf-8')
with open(path4, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut5, 'w', encoding='utf-8')
with open(path5, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass
fout.close()

path11 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_fieldID_fieldName_HIndex(11years).txt"
path22 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_fieldID_fieldName_paperCnt(11years).txt"
path33 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sortedName_JIF(11years).txt"
path44 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sorteName_fieldID_fieldName_aveCitation(11years).txt"
path55 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter\affID_sorteName_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt"

pathOut11 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_HIndex(11years).txt"
pathOut22 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_fieldID_fieldName_paperCnt(11years).txt"
pathOut33 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_JIF(11years).txt"
pathOut44 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years).txt"
pathOut55 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sorteName_LMH_fieldID_fieldName_aveCitation(11years_buChuYiLunWenShu).txt"

fout = open(pathOut11, 'w', encoding='utf-8')
with open(path11, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut22, 'w', encoding='utf-8')
with open(path22, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut33, 'w', encoding='utf-8')
with open(path33, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut44, 'w', encoding='utf-8')
with open(path44, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass
fout.close()

fout = open(pathOut55, 'w', encoding='utf-8')
with open(path55, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        fout.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass
fout.close()
###########################################################################
# 合作者强度和合作者数两个文件
###########################################################################

path1 = r"C:\Users\12433\Desktop\data11years\dz\dzFxID_assumeAwardYear_aveCIIBF_aveCIIAF.txt"
path2 = r"C:\Users\12433\Desktop\data11years\dz\dzFxID_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"
pathOut1 = r"C:\Users\12433\Desktop\data11years\dz\filter1\dzFxID_LMH_assumeAwardYear_aveCIIBF_aveCIIAF.txt"
pathOut2 = r"C:\Users\12433\Desktop\data11years\dz\filter1\dzFxID_LMH_dzAwardYear_dzCoAuthorsNumBF_dzCoAuthorsNumAF.txt"
xxx = list()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        xxx.append(line)
    pass
with open(pathOut1, 'w', encoding='utf-8') as f:
    f.write("dzFxID\tL\tM\tH\tassumeAwardYear\taveCIIBF\taveCIIAF\n")
    for line in xxx[1:]:
        f.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass

xxx = list()
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        xxx.append(line)
    pass
with open(pathOut2, 'w', encoding='utf-8') as f:
    f.write("dzFxID\tL\tM\tH\tdzAwardYear\tdzCoAuthorsNumBF\tdzCoAuthorsNumAF\n")
    for line in xxx[1:]:
        f.write(line[0]+'\t'+'\t'.join(dz_LMH_dict[(line[0])])+'\t'+'\t'.join(line[1:])+'\n')
        pass
    pass



path11 = r"C:\Users\12433\Desktop\data11years\jq\affID_sortedName_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
path22 = r"C:\Users\12433\Desktop\data11years\jq\affID_sortedName_aveCIIBF_aveCIIAF.txt"
pathOut11 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_awardYear_coAuthorsNumBF_coAuthorsNumAF.txt"
pathOut22 = r"C:\Users\12433\Desktop\data11years\jq\jq_filter1\affID_sortedName_LMH_aveCIIBF_aveCIIAF.txt"

xxx = list()
with open(path11, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        xxx.append(line)
    pass
with open(pathOut11, 'w', encoding='utf-8') as f:
    f.write("affID\tsortedName\tL\tM\tH\tawardYear\tcoAuthorsNumBF\tcoAuthorsNumAF\n")
    for line in xxx[1:]:
        f.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass

xxx = list()
with open(path22, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        xxx.append(line)
    pass
with open(pathOut22, 'w', encoding='utf-8') as f:
    f.write("affID\tsortedName\tL\tM\tH\taveCIIBF\taveCIIAF\n")
    for line in xxx[1:]:
        f.write(line[0]+'\t'+line[1]+'\t'+'\t'.join(jq_LMH_dict[(line[0], line[1])])+'\t'+'\t'.join(line[2:])+'\n')
        pass
    pass
