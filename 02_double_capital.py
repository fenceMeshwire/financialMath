#!/usr/bin/env python3

# Python 3.9.5

# Dependencies
import numpy as np
import matplotlib.pyplot as plt

# Calculation:
interest_rate = np.linspace(1.01, 1.1, 100)
years_to_double = [np.log(2) / np.log(rate) for rate in interest_rate]

# Visualization:
fig, ax = plt.subplots()

ax.plot(years_to_double)
ax.set_xticks([i for i in range(0, 110, 10)])
ax.set_xticklabels([j for j in range(0, 11, 1)])

ax = plt.xlabel("Interest Rate in Percent [%]")
ax = plt.ylabel("Years for Doubling of Capital invested")

plt.show()
