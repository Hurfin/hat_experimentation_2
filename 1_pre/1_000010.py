# -*- coding: utf-8 -*-
# !/usr/bin/env python

path = r"C:\Users\12433\Desktop\1_affiliationID_authorEnglishName_minYear_awardYear_academicAge.txt"

DICT_affiliationID_name__minYear_awardYear = {}

with open(path, "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        line = line.split('\t')
        name_list = line[1].split(' ')
        name_list.sort()
        name = ' '.join(name_list)
        author = line[0] + '\t' + name
        if author not in DICT_affiliationID_name__minYear_awardYear.keys():
            DICT_affiliationID_name__minYear_awardYear[author] = {
                'minYear': int(line[2]),
                'awardYear': int(line[3])
            }
        else:
            if DICT_affiliationID_name__minYear_awardYear[author]['minYear'] > int(line[2]):
                DICT_affiliationID_name__minYear_awardYear[author]['minYear'] = int(line[2])
path2 = r"C:\Users\12433\Desktop\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge.txt"
with open(path2, "w", encoding='utf-8') as f:
    for author, minYear_awardYear in DICT_affiliationID_name__minYear_awardYear.items():
        if (minYear_awardYear['awardYear'] - minYear_awardYear['minYear']) < 0:
            continue
        f.write(author+'\t'+str(minYear_awardYear['minYear'])+'\t'+str(minYear_awardYear['awardYear'])+'\t'+str(minYear_awardYear['awardYear']-minYear_awardYear['minYear'])+'\n')
