#!/usr/bin/env python3

# Python 3.9.5

# 01_obtain_stock_information.py

# Dependency
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
yf.pdr_override()
from datetime import datetime

# Obtain data
complete_data = {str(tc): pdr.get_data_yahoo(str(tc)) for tc in ['MO', 'T', 'GOGL', 'C']}

# Create a DataFrame from complete_data
price = pd.DataFrame({tc: data['Adj Close'] for tc, data in complete_data.items()})

# Change the display output to e.g.: 9.98$
pd.options.display.float_format = '{:,.2f}$'.format

# Print the last five records of the DataFrame
print(price.tail())
