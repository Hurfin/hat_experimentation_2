# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算r"E:\FengXu\result1\coAuthorJournalID(needToCompute).txt"中的这部分JIF
得到r"E:\FengXu\result\JIF\(coAuthorNeedToCompute)journalID_JIF_perYear_from1989to2017.txt"


年份从1989-2019
path1 = r"E:\FengXu\result1\coAuthorJournalID(needToCompute).txt"
path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
path3 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
pathOut = r"E:\FengXu\result\JIF\(coAuthorNeedToCompute)journalID_JIF_perYear_from1989to2017.txt"
"""
import pandas as pd
from collections import defaultdict
from time import time


def getReference():
    referenceID_year_citationCnt_DICT = defaultdict(lambda: 0)
    yearList = list(range(1989, 2018))
    for year in yearList:
        path_i = r"E:\FengXu\result\JIF\referenceID_citationCnt_perYear\referenceID_citationCnt({}).txt".format(year)
        with open(path_i, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().split('\t')
                referenceID_year_citationCnt_DICT[(line[0], year)] = int(line[1])
    return referenceID_year_citationCnt_DICT


def main():
    path1 = r"E:\FengXu\result1\coAuthorJournalID(needToCompute).txt"
    path2 = r"E:\FengXu\result\JIF\paperID_year_journalID(papersJournal).txt"
    # path3 = r"E:\FengXu\result\JIF\paperID_referenceID(papersJournal).txt"
    pathOut = r"E:\FengXu\result\JIF\(coAuthorNeedToCompute)journalID_JIF_perYear_from1989to2017.txt"

    referenceID_year_citationCnt_DICT = getReference()

    journalID_list = pd.read_csv(path1, sep='\t', header=None, names=['journalID'])
    paperID_year_journalID = pd.read_csv(path2, sep='\t', header=None, names=['paperID', 'year', 'journalID'])

    fout = open(pathOut, "w", encoding='utf-8')
    cnt = 0
    for i in range(len(journalID_list)):
        start1 = time()
        journalID_i = journalID_list.iloc[i]['journalID']
        papers_i = paperID_year_journalID[paperID_year_journalID['journalID'] == journalID_i]
        end1 = time()
        """ 第一段计时 """
        print(journalID_i, str(end1-start1))
        YearList = list(range(1989, 2018))
        fout.write(str(journalID_i))
        for year in YearList:
            """ 第二段计时 """
            start2 = time()
            papersBeforeYear1 = papers_i[papers_i['year'] == (year - 1)]
            papersBeforeYear2 = papers_i[papers_i['year'] == (year - 2)]
            n1_sum_n2 = papersBeforeYear1.shape[0] + papersBeforeYear2.shape[0]
            end2 = time()
            print(year, str(end2-start2), end='\t')

            papersBeforeYear1_paperID = papersBeforeYear1[['paperID']]
            papersBeforeYear2_paperID = papersBeforeYear2[['paperID']]

            sum_JournalCitations_thisYear = 0
            """ 每次在这个大文件中去查找一个paper id被引用多少次，可以提前计算好每年该文章的被引用次数，使用时直接读取 """
            """ 第三段计时 """
            start3 = time()
            for k in range(len(papersBeforeYear1_paperID)):
                paperID_x1 = papersBeforeYear1_paperID.iloc[k]['paperID']
                paperID_x1 = str(int(float(paperID_x1)))
                sum_JournalCitations_thisYear += referenceID_year_citationCnt_DICT[
                    (paperID_x1, year)]

            for k in range(len(papersBeforeYear2_paperID)):
                paperID_x2 = papersBeforeYear2_paperID.iloc[k]['paperID']
                paperID_x2 = str(int(float(paperID_x2)))
                sum_JournalCitations_thisYear += referenceID_year_citationCnt_DICT[
                    (paperID_x2, year)]
                pass
            end3 = time()
            print(str(end3-start3))
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
