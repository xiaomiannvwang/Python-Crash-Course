#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:20:42 2018

@author: sk
"""

import matplotlib.pyplot as plt
"""
x_value = [0, 1,2, 3, 4, 5]
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value)
"""
x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]

plt.title("cube", fontsize=24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("cube of value", fontsize = 14)

plt.tick_params

plt.scatter(x_value, y_value, c=(0.9, 0.5, 0.9), edgecolor = 'none', s=10)
