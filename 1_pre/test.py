# -*- coding: utf-8 -*-
# !/usr/bin/env python

# path = r"C:\Users\12433\Desktop\awardYear_englishName_affID_chineseName.txt"
# l = []
# with open(path, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         l.append(line)
# l = list(set(l))
#
# with open(r"E:\pythonCode\RJ_experimentation_1\Data\awardYear_englishName_affID_chineseName.txt", "w", encoding='utf-8') as f:
#     for line in l:
#         f.write(line+"\n")
# x = '1234123.0'
# x = float(x)
# print(int(x))

x = '冯旭 iasdfF'

# for i in x:
#     if not ((i>='a' and i<='z') or (i>='A' and i<='Z') or (i==' ')):
#         print("汉字")
#     else:
#         print("字母或空格")

# for i in x:
#     if i < u'\u4e00' or i > u'\u9fff':
#         print("OK", i)
#     if i>=u'\u4e00' and i<=u'\u9fff':
#         print('汉字', i)
# x = [0, 'asd', '23']
# try:
#     xx='\t'.join(x)
# except Exception as e:
#     print(e)
#     print(x)
import copy
# x = [1, 2, 3, 4]
# xx = [x, 'a']
# # y = copy.deepcopy(xx)
# y = xx
# # y[0][0] = 2
# # y[1] = 'b'
# xx[0][0] = 3
# print(xx)
# print(y)

import pickle
path = r"C:\Users\12433\Desktop\1_affiliationID_authorEnglishName_minYear_awardYear_academicAge.txt"
xx = ['asdf']
print(' '.join(xx))
