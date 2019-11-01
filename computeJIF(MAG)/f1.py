# -*- coding: utf-8 -*-
# !/usr/bin/env python

# import pandas as pd
#
# path = r'E:\pythonCode\RJ_experimentation_1\Data\result\2_paperYear_sub_awardYear_paperCnt.txt'
# data = pd.read_csv(path, sep=' ', header=None, names=['x', 'y'])
# # print(data)
# # data = list(data)
# # print(data)
# # for x in data:
# #     print(x)
#
# for i in range(len(data)):
#     print(data.iloc[i]['x'], data.iloc[i]['y'])

# from collections import defaultdict
#
# dd = defaultdict(lambda: 0)
# print(dd[('a', 1)])
from time import time

start = time()
for i in range(10000000):
    pass
end = time()
print(end-start)