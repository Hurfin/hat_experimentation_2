# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np
def fun(x):
    if x['Ki'] == 0 or x['Kj'] == 0 or x['Kij'] == 0:
        return 0
    return x['Kij']/(x['Ki']*x['Kj'])

path1 = r"E:\FengXu\result\TMP\JQ_affiliationID_JQ_sortedName_CO_authorID_" \
          r"JQ_awardYear_Ki_Kj_kij_flag(before1_after0).txt"
names = ['JQ_affiliationID', 'JQ_sortedName', 'CO_authorID', 'JQ_awardYear', 'Ki', 'Kj', 'Kij', 'flag']
data = pd.read_csv(path1, sep='\t', header=None, names=names)
data['CII'] = data.apply(fun, axis=1)
pathOut = r"E:\FengXu\result\TMP\ans_CII(flag_before_1_after_0).txt"
data = data.drop(['JQ_awardYear'], axis=1)
data.to_csv(pathOut, sep='\t', index=False)
