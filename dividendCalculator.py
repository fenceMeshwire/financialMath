#!/usr/bin/env python3

# Python 3.9.5

# dividendCalculator.py

# Dependencies
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
import os
from pathlib import Path
from sklearn.linear_model import LinearRegression

# Change Working Directory
def changePath():
    # the path for the input file goes here. Single column of values (s. stockDividend.txt)
    path = '/home/user/downloads'
    os.chdir(path)
    return Path.cwd()

changePath()

# Data AT&T
with open('stockDividend.txt', 'rt', encoding='utf-8') as data:
    dividend = np.genfromtxt(data, dtype=float, delimiter=',')
print(dividend)
quarters = [i for i in range(len(dividend), 0, -1)]

# Print max, min, mean and var
print(np.max(dividend))
print(np.min(dividend))
print(np.mean(dividend))
print(np.var(dividend))

n = len(dividend)
# process the data with linear regression:
model = LinearRegression().fit(np.arange(n).reshape((n, 1)), dividend)
print(model.predict([[n], [1]]))

plt.plot(quarters, dividend, linestyle='--', marker='o', color='orange')
plt.plot([1, n], model.predict([[n], [1]]))
plt.title('Company: Quarters vs. Dividend')
plt.xlabel('Quarters')
plt.ylabel('Dividend per share in US-Dollar')
plt.show()
