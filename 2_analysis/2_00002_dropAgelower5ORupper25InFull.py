# -*- coding: utf-8 -*-
# !/usr/bin/env python

def check(normalizedName, nameSorted):
    normalizedName_list = normalizedName.split(' ')
    normalizedName_list.sort()
    normalizedName = ' '.join(normalizedName_list)
    if normalizedName == nameSorted:
        return True
    else:
        return False
    pass

def main():
    path = r"E:\FengXu\result\dropSameOrg_sameEnglishName_JieQing_paperID_authorID_affiliationID_paperYear_normal" \
           r"izedName_displayName_chineseName_awardYear.txt"
    path1 = r"E:\FengXu\result\dropSameOrg_sameEnglishName_academicAgeFrom5to25_JieQing_paperID_authorID_affiliationID" \
            r"_paperYear_normalizedName_displayName_chineseName_awardYear.txt"
    path2 = r"E:\FengXu\result\HPData\2_affiliationID_authorEnglishNameSorted_minYear_awardYear_academicAge" \
            r"(age_lower5_upper25).txt"

    People_age_lower5_upper25 = []
    # 学术年龄超出界外的人
    with open(path2, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.split('\t')
            People_age_lower5_upper25.append(line)
        pass

    fout = open(path1, 'w', encoding='utf-8')
    # full doc
    with open(path, 'r', encoding='utf-8') as f:  # full doc
        for line in f:
            line = line.strip()
            line = line.split('\t')
            affID = line[2]
            normalizedName = line[4]
            flag = 0
            for People_age_lower5_upper25_i in People_age_lower5_upper25:
                nameSorted = People_age_lower5_upper25_i[1]
                affID1 = People_age_lower5_upper25_i[0]
                if affID != affID1:
                    continue
                if check(normalizedName, nameSorted) is False:
                    continue
                flag = 1
                break
            if flag == 1:
                continue
            else:
                fout.write('\t'.join(line)+'\n')
        pass
    fout.close()


if __name__ == "__main__":
    main()
    pass
