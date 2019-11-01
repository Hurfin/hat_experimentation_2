# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算各期刊各年份的JIF
年份从1989-2019
path1 = r"E:\FengXu\result\JIF\JieqingContribute_JournalID.txt"
path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
path3 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
pathOut = r"E:\FengXu\result\JIF\journalID_JIF_perYear_from1989to2019.txt"
"""
import pandas as pd


def main():
    path1 = r"E:\FengXu\result\JIF\JieqingContribute_JournalID.txt"
    path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
    path3 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
    pathOut = r"E:\FengXu\result\JIF\journalID_JIF_perYear_from1989to2019.txt"

    journalID_list = pd.read_csv(path1, sep='\t', header=None, names=['journalID'])
    paperID_year_journalID = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'year', 'journalID'])
    paperID_referenceID = pd.read_csv(path3, sep='\t', header=None, names=['paperID', 'referenceID'])
    fout = open(pathOut, "w", encoding='utf-8')
    cnt = 0
    for i in range(len(journalID_list)):
        journalID_i = journalID_list.iloc[i]['journalID']
        papers_i = paperID_year_journalID[paperID_year_journalID['journalID'] == journalID_i]
        YearList = list(range(1989, 2020))
        fout.write(str(journalID_i))
        for year in YearList:
            papersBeforeYear1 = papers_i[papers_i['year'] == (year - 1)]
            papersBeforeYear2 = papers_i[papers_i['year'] == (year - 2)]
            n1_sum_n2 = papersBeforeYear1.shape[0] + papersBeforeYear2.shape[0]
            papersID_this_year = paperID_year_journalID[paperID_year_journalID['year'] == year][['paperID']]
            """ 可以提前计算好每年该文章的被引用次数，使用时直接读取，就不用每次计算该年所有的paper id，以及对应的reference id（计算时一定要同时多个年份一起跑，试试多线程或者写多个脚本同时跑） """
            paperIDThisYear_referenceID = paperID_referenceID.merge(papersID_this_year, on='paperID', how='inner')
            paperIDThisYear_referenceID = paperIDThisYear_referenceID[['paperID', 'referenceID']]

            papersBeforeYear1_paperID = papersBeforeYear1[['paperID']]
            papersBeforeYear2_paperID = papersBeforeYear2[['paperID']]
            """ concact()可以考虑取消掉，代替用两个for循环，分别去计算sum_JournalCitations_thisYear。(因为不同年份，paper id不太可能会重复，所以去重操作也取消掉) """
            papersBeforeYear_1_2_paperID = pd.concat([papersBeforeYear1_paperID, papersBeforeYear2_paperID],
                                                     ignore_index=True)
            # papersBeforeYear_1_2_paperID = papersBeforeYear_1_2_paperID.drop_duplicates()
            del papersBeforeYear1_paperID, papersBeforeYear2_paperID, papersBeforeYear1, papersBeforeYear2
            sum_JournalCitations_thisYear = 0
            for k in range(len(papersBeforeYear_1_2_paperID)):
                """ 每次在这个大文件中去查找一个paper id被引用多少次，可以提前计算好每年该文章的被引用次数，使用时直接读取 """
                sum_JournalCitations_thisYear += \
                    paperIDThisYear_referenceID[
                        paperIDThisYear_referenceID['referenceID'] == papersBeforeYear_1_2_paperID.iloc[k]['paperID']
                        ].shape[0]
            JIF_thisJournal_thisYear = 0
            if n1_sum_n2 == 0:
                JIF_thisJournal_thisYear = 0
            else:
                JIF_thisJournal_thisYear = sum_JournalCitations_thisYear / n1_sum_n2
            fout.write('\t' + str(JIF_thisJournal_thisYear))
        fout.write('\n')
        cnt += 1
        print(cnt, "journal:", journalID_i, "is OK")
    fout.close()


if __name__ == '__main__':
    main()
    pass
