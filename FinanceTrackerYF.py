# 25 April 2019
# Created by R. Krutz
import pandas as pd
import csv
import stockHistoryYF as shyf


a = pd.read_csv('YOURFILEHERE.csv')

print(a['ticker'][1])
print(type(a['ticker'][1]))
'''

with open('YOURFILEHERE.csv', 'r') as f:
    reader = csv.reader(f)
    stock = list(reader)
#print(stock)
x = 1
for value in stock:
    #print(stock[x])
    shyf.stockHistoryYF(stock[x],'YYYY-MM-DD', 'YYYY-MM-DD')
    #print('------------')
    x = x+1

print('FINISHED')
