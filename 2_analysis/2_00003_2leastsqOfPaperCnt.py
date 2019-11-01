# -*- coding: utf-8 -*-
# !/usr/bin/env python

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def err(p, x, y):
    return p[0] * x + p[1] - y

# 左侧图
p0 = [100, 100]
Xi = np.array([-5, -4, -3, -2, -1])
Yi = np.array([5023, 6034, 7502, 8907, 10322])
# Xi = np.array([-5, -4, -3, -2, -1, 0])
# Yi = np.array([5023, 6034, 7502, 8907, 10322, 11571])
ret = leastsq(err, p0, args=(Xi, Yi))
print(ret)

k, b = ret[0]
plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color='red', label='Point1', linewidth=3)
x = np.linspace(-5, 0, 1000)
y = k * x + b
plt.plot(x, y, color='orange', label='Fitting Line1', linewidth=2)

# 右侧图
p0 = [100, 100]
Xi = np.array([1, 2, 3, 4, 5])
Yi = np.array([12213, 13371, 14817, 14058, 12800])
# Xi = np.array([0, 1, 2, 3, 4, 5])
# Yi = np.array([11571, 12213, 13371, 14817, 14058, 12800])
ret = leastsq(err, p0, args=(Xi, Yi))
print(ret)

k, b = ret[0]
# plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color='blue', label='Point2', linewidth=3)
x = np.linspace(0, 5, 1000)
y = k * x + b
plt.plot(x, y, color='red', label='Fitting Line2', linewidth=2)


plt.legend()
plt.show()


