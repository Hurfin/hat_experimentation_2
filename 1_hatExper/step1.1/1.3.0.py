# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
预先处理引用数据
"""
import pandas as pd
import os

path = r"E:\pythonCode\RJ_experimentation_1\Data_1\ref\paperID_refID_paperYear(refJQ).txt"
data = pd.read_csv(path, sep='\t', header=None, names=['paperID', 'refID', 'paperYear'])
data = data.groupby(['refID', 'paperYear'])['paperID'].count()
data = data.reset_index()
data.columns = ['refID', 'paperYear', 'thisYearCitationCnt']
path_out = r"E:\pythonCode\RJ_experimentation_1\Data_1\ref\refID_paperYear_thisYearCitationCnt.txt"
data.to_csv(path_out, header=None, index=None, sep='\t')
