#!/usr/bin/env python

# Python 3.9.5

# billing_VAT_lineup.py

# Purpose: Calculate the cumulative total for a receipt if there are commodity groups with different tax rates.

# Dependencies:
import csv
import os
from pathlib import Path

# Determine your working directory:
file = os.path.join(Path.cwd(), 'directory/sub_directory/...')
os.chdir(file)

articles:dict = [];     net_price:dict = []
grp_drinks:float = 0;   grp_food:float = 0
nets_drinks:float = 0;  vats_drinks:float = 0
nets_foods:float = 0;   vats_foods:float = 0
sum_net:float = 0;      sum_gross:float = 0

def calc_VAT(vat_factor, gross_price):
    vat_vactor_drinks:float = 1.19; vat_factor_food:float = 1.07 
    net_price_drinks:float = 0;     net_price_food:float = 0
    vat_drinks:float = 0;           vat_food:float = 0
    if vat_factor == 19:
        net_price_drinks = float(gross_price) / float(vat_vactor_drinks)
        vat_drinks = net_price_drinks * (vat_vactor_drinks - 1)
    elif vat_factor == 7:
        net_price_food = float(gross_price) / float(vat_factor_food)
        vat_food = net_price_food * (vat_factor_food - 1)
    return net_price_drinks, net_price_food, vat_drinks, vat_food

# Input file is restaurant.csv in this repository
with open('restaurant.csv', newline='') as csv_import:
    line = csv.reader(csv_import, delimiter='\n')
    for row in line:
        elements = row[0].split(',')
        articles.append(elements)

for article in articles:
    if not article[0][0].isnumeric():
        articles.pop(0)
    
for article in articles:
    # Select values from row
    vat_factor = int(article[3]); qty = float(article[0])
    gross_price = float(article[4]) * qty
    net_price = gross_price / vat_factor
    sum_gross += gross_price
    # Calculate VAT factor and gross price
    net_price_drinks, net_price_food, vat_drinks, vat_food = \
    calc_VAT(vat_factor, gross_price)
    # Calculate the cumulative total for the lineup
    nets_drinks += net_price_drinks;    nets_foods += net_price_food
    vats_drinks += vat_drinks;          vats_foods += vat_food
    grp_drinks = grp_drinks + net_price_drinks + vat_drinks
    grp_food = grp_food + net_price_food + vat_food

# Format the floating point numbers
sum_gross = format(sum_gross, '0.2f')
gross_price_food = format(grp_food, '0.2f');    gross_price_drinks = format(grp_drinks, '0.2f')
nets_drinks = format(nets_drinks, '0.2f');      nets_foods = format(nets_foods, '0.2f')
vats_drinks = format(vats_drinks, '0.2f');      vats_foods = format(vats_foods, '0.2f')

# Print the output
print('Gross sum all articles:', sum_gross)
print('Gross price food:', gross_price_food);       print('Gross price drinks:', gross_price_drinks)
print('Value added tax for drinks:', vats_drinks);  print('Value added tax for food:', vats_foods)
print('Net price for drinks:', nets_drinks);        print('Net price for food:', nets_foods)
