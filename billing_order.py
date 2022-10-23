#!/usr/bin/env python3

# Python 3.9.5

# billing_order.py

# Dependency
import pandas as pd

# cat: category
# art: article
# ppu: price per unit
# cpu: cumulated price per unit
# qty: quantity

columns = pd.Series(['cat', 'art', 'ppu', 'cpu', 'qty'])
columns
order = [
    {'cat': 1, 'art': 'beer', 'ppu': 4.2, 'cpu': 4.2, 'qty': 1},
    {'cat': 1, 'art': 'water', 'ppu': 1.8, 'cpu': 1.8, 'qty': 1},
    {'cat': 1, 'art': 'water big', 'ppu': 3.0, 'cpu': 3.0, 'qty': 1},
    {'cat': 1, 'art': 'juice', 'ppu': 3.9, 'cpu': 3.9, 'qty': 1},
    {'cat': 1, 'art': 'main dish 1', 'ppu': 13.5, 'cpu': 13.5, 'qty': 1},
    {'cat': 1, 'art': 'main dish 2', 'ppu': 15.5, 'cpu': 15.5, 'qty': 1}
    ]

order = pd.DataFrame(order, columns=columns)
print(order)

# Accessing the named columns:
order.cat
order.art
order.ppu
order.cpu
order.qty

total = sum(order.cpu)
print(total) # Print total amount from cumulated price of all units.

order.iloc[0:1] # Accessing the first row.
order.values # Accessing the values.

order[order.ppu < 3] # List order element, where ppu < 3
order[order.ppu > 15] # List order element, where ppu > 15

# Optional: Store output as CSV file:
import os

path = 'C:\\...\\...'
os.chdir(path)

order.to_csv('order.csv', index=None)
