# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
[1, 2, 3, 4, 5]
[12213, 13371, 14817, 14058, 12800]
"""
# Xi = [-5, -4, -3, -2, -1]
# Yi = [5023, 6034, 7502, 8907, 10322]

Xi = [1, 2, 3, 4, 5]
Yi = [12213, 13371, 14817, 14058, 12800]

# Xi = [-5, -4, -3, -2, -1, 0]
# Yi = [5023, 6034, 7502, 8907, 10322, 11571]
#
# Xi = [0, 1, 2, 3, 4, 5]
# Yi = [11571, 12213, 13371, 14817, 14058, 12800]
import time
from scipy.optimize import leastsq
import numpy as np


def err(p, x, y):
    return p[0] * x + p[1] - y


def leastSqrt(Xi, Yi):
    sum_xi_yi = 0
    sum_xi = 0
    sum_yi = 0
    sum_xi_sq = 0
    n = len(Xi)
    for i in range(0, len(Xi)):
        sum_xi_yi += Xi[i] * Yi[i]
        sum_xi += Xi[i]
        sum_yi += Yi[i]
        sum_xi_sq += Xi[i] * Xi[i]
    k = (n * sum_xi_yi - sum_xi * sum_yi) / (n * sum_xi_sq - sum_xi * sum_xi)
    b = (sum_yi - k * sum_xi) / n
    return k, b

a1 = 0
a2 = 0


start = time.process_time()
for i in range(0, 100000):
    sum_xi_yi = 0
    sum_xi = 0
    sum_yi = 0
    sum_xi_sq = 0
    for i in range(0, len(Xi)):
        sum_xi_yi += Xi[i] * Yi[i]
        sum_xi += Xi[i]
        sum_yi += Yi[i]
        sum_xi_sq += Xi[i] * Xi[i]

    n = len(Xi)

    a1 = (n * sum_xi_yi - sum_xi * sum_yi) / (n * sum_xi_sq - sum_xi * sum_xi)
    # print(a1)

    a2 = (sum_yi - a1 * sum_xi) / n
    # print(a2)
end = time.process_time()
print(end - start)
print(a1, a2)

Xi = [1, 2, 3, 4, 5]
Yi = [12213, 13371, 14817, 14058, 12800]

p0 = [100, 100]
k=0
b=0
start = time.process_time()
Xi = np.array(Xi)
Yi = np.array(Yi)
for i in range(0, 100000):
    ret = leastsq(err, p0, args=(Xi, Yi))
    k, b = ret[0]
end = time.process_time()
print(end - start)
print(k, b)
