import pygal
import lxml
import requests

print('-------Stock Data Visualizer-------')

print('Enter the stock symbol you are looking for: ')
stockSymbol = input()


print('Enter the chart type you want (1,2): ')
chartType = input()

print('''
Select the Time Series of the chart you want to Generate
--------------------------------------------------------
1.
2.
3.
4.

Enter time series option (1, 2, 3, 4):
''')
timeSeries = input()

print('Enter the start Date (YYYY-MM-DD): ')
startDate = input()

print('Enter the end Date (YYYY-MM-DD): ')
endDate = input()


#Chart opens here


