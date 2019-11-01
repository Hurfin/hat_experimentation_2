# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv(r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\dataMerge.txt", sep='\t', index_col=[0])

# print(data.describe())
pathOut = r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\linearRegression_ans.txt"
f = open(pathOut, 'a', encoding='utf-8')
model1 = LinearRegression()
model1.fit(data[['L', 'M', 'H', 'award']], data[['aveCitationCnt']])
print(model1.coef_, model1.intercept_, "aveCitationCnt", file=f)

model2 = LinearRegression()
model2.fit(data[['L', 'M', 'H', 'award']], data[['aveJIF']])
print( model2.coef_, model2.intercept_, "aveJIF", file=f)

model3 = LinearRegression()
model3.fit(data[['L', 'M', 'H', 'award']], data[['aveH-Index']])
print( model3.coef_, model3.intercept_, "aveH-Index", file=f)

model4 = LinearRegression()
model4.fit(data[['L', 'M', 'H', 'award']], data[['avePaperCnt']])
print(model4.coef_, model4.intercept_, "avePaperCnt", file=f)
f.write('\n')
f.close()



# x = []
# x.append(model1.coef_)
# x.append(model2.coef_)
# x.append(model3.coef_)
# x.append(model4.coef_)
ans_ = {}
ans_['aveCitationCnt'] = model1.coef_[0]
ans_['aveJIF'] = model2.coef_[0]
ans_['aveH-Index'] = model3.coef_[0]
ans_['avePaperCnt'] = model4.coef_[0]
ans_DF = pd.DataFrame(ans_, index=['L', 'M', 'H', 'award'])

ans_DF.to_csv(r"E:\pythonCode\RJ_experimentation_1\Data\compareGroupData\divideGroup\JQ_DZ_1To1\ans_1\linearRegression_ans1.txt",
            sep='\t')
