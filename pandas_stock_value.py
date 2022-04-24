#!/usr/bin/env python3

# Python 3.9.5

# pandas_stock_value.py

# Dependencies
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

# Data: Stock values for AT&T:
at_t = data.DataReader('T', start='2012', end='2022', data_source='yahoo')
at_t.head()

at_t = at_t['Close']

# Resampling frequencies
at_t.plot(alpha=0.5, style='-')
at_t.resample('BA').mean().plot(style=':')
at_t.asfreq('BA').mean
plt.legend(['input', 'resample', 'asfreq'], loc='upper left')

# Show diagram
plt.show()
