# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
计算
"""
import pandas as pd
# path0 = r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"
# path1 = r"D:\Dataset\NEW_MAG\PaperAuthorAffiliations.txt"
# # 需要dz组的合作者的全部论文信息（paperID、paperYear、以及paperID对应的合作者的authorID）
#
# dzCoAuthorID_set = set()
# with open(path0, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         dzCoAuthorID_set.add(line[1])
#         pass
#     pass
#
# fout = open(r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID.txt", 'w', encoding='utf-8')
# with open(path1, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         if line[1] in dzCoAuthorID_set:
#             fout.write(line[0]+'\t'+line[1]+'\n')
#         pass
#     pass
# fout.close()

# path0 = r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID.txt"
# path1 = r""
# dzCoCoPaperID_set = set()
# with open(path0, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         dzCoCoPaperID_set.add(line[0])
#         pass
#     pass
# fout = open(r"E:\FengXu\result3\dzCoCoPaperID_PYear.txt", 'w', encoding='utf-8')
# with open(r"D:\Dataset\NEW_MAG\Papers.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         if line[0] in dzCoCoPaperID_set:
#             if line[7] != '' or line[7] is not None:
#                 fout.write(line[0] + '\t' + line[7] + '\n')
#             else:
#                 print(line)
#         pass
#     pass
# fout.close()


# path0 = r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID.txt"
# path1 = r"E:\FengXu\result3\dzCoCoPaperID_PYear.txt"
#
# dzCoCoPaperID_PYear = dict()
# with open(path1, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         dzCoCoPaperID_PYear[line[0]] = line[1]
#         pass
#     pass
#
# fout = open(r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID_PYear.txt", 'w', encoding='utf-8')
# with open(path0, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         if line[0] in dzCoCoPaperID_PYear.keys():
#            fout.write('\t'.join(line)+'\t'+dzCoCoPaperID_PYear[line[0]]+'\n')
#         else:
#             print(line)
#     pass
# fout.close()

# path0 = r"E:\FengXu\result3\dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"
#
# dzAffID_dzNormalizedName_index = dict()
# dzCoAuthorID_index = dict()
# cnt = 0
# fout = open(r"E:\FengXu\result3\dzCoFxID_dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt", 'w', encoding='utf-8')
# with open(path0, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip('\n').split('\t')
#         if (line[2], line[3]) not in dzAffID_dzNormalizedName_index.keys():  # 如果（affID, normalizedName）没有记录的话
#             if line[1] in dzCoAuthorID_index.keys(): # 那就看coAuthor里有没有被记录过
#                 # 如果记录过的话就把coAuthor对应的编号给它
#                 dzAffID_dzNormalizedName_index[(line[2], line[3])] = dzCoAuthorID_index[line[1]]
#             else:  # 如果coAuthor里没有记录过的话
#                 dzAffID_dzNormalizedName_index[(line[2], line[3])] = cnt
#                 dzCoAuthorID_index[line[1]] = cnt
#                 cnt += 1
#             pass
#         else:  # 如果（affID，normalized）已经有记录了
#             dzCoAuthorID_index[line[1]] = dzAffID_dzNormalizedName_index[(line[2], line[3])]
#             pass
#         fout.write(str(dzAffID_dzNormalizedName_index[(line[2], line[3])])+'\t'+'\t'.join(line)+'\n')
#         pass
#     pass
# fout.close()

path0 = r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID_PYear.txt"
path1 = r"E:\FengXu\result3\dzCoFxID_dzPaperID_dzCoAuthorID_dzAffID_dzNormalizedName.txt"
dzCoAuthorID_dzFXID_dict = dict()
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        dzCoAuthorID_dzFXID_dict[line[2]] = line[0]
        pass
    pass

fout = open(r"E:\FengXu\result3\dzCoCoPaperID_dzCoAuthorID_dzCoFxID_PYear.txt", 'w', encoding='utf-8')
with open(path0, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n').split('\t')
        if line[1] in dzCoAuthorID_dzFXID_dict.keys():
            fout.write(line[0]+'\t'+line[1]+'\t'+dzCoAuthorID_dzFXID_dict[line[1]]+'\t'+line[2]+'\n')
        else:
            print(line)
    pass
fout.close()
