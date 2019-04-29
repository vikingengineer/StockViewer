import pandas as pd
import csv
import stockHistoryYF as shyf

'''
a = pd.read_csv('OneSourceETFListTest.csv')
#a =  pd.read_csv('OneSourceETFListTest.csv').to_dict()
print(a['ticker'][1])
print(type(a['ticker'][1]))
'''
#stock = ['AAPL', 'GOOGL', 'GM', 'F']
with open('OneSourceETFListTest.csv', 'r') as f:
    reader = csv.reader(f)
    stock = list(reader)
#print(stock)
x = 1
for value in stock:
    #print(stock[x])
    shyf.stockHistoryYF(stock[x],'2019-04-08', '2019-04-20')
    #print('------------')
    x = x+1

print('FINISHED')
