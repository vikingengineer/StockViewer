# StockViewer

Python program to track a stocks daily open and close value over a given period of time and to see the delta from each day of trading.
Function found in stockHistoryYF.py takes stock name, start date (YYYY-MM-DD) and end date (YYYY-MM-DD) and uses the fix_yahoo_finance library to do the backend work.  From this it will plot the open and close value from each working day in the timeframe you supplied.  It will also plot the delta of the open and close value for each open day on another graph to see how the stock is moving.  Then it will print the Yahoo FInance data to a CSV file and save the photos to a .png.

The FinanceTrackerYF.py program takes the function and allows you to run it against a csv file holding multiple stock tickers.

Useful reading for this project is as follows:
https://aroussi.com/post/python-yahoo-finance
https://learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/
https://www.quantinsti.com/blog/build-technical-indicators-in-python

*Please note that the code is still a current work in progress and not a final product. Use at your own risk.
