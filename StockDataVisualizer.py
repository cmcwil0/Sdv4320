import pygal
import lxml
import requests

print('-------Stock Data Visualizer-------')

print('Enter the stock symbol you are looking for: ')
stockSymbol = input()

print('''
Chart Types
-----------
1. Bar
2. Line
      
Enter the chart type you want (1,2): ''')
chartType = input()

print('''
Select the Time Series of the chart you want to Generate
--------------------------------------------------------
1. Intraday
2. Daily
3. Weekly
4. Monthly

Enter time series option (1, 2, 3, 4):''')
timeSeries = input()

print('Enter the start Date (YYYY-MM-DD): ')
startDate = input()

print('Enter the end Date (YYYY-MM-DD): ')
endDate = input()


#Chart opens here


#after chart opens

print('Would you like to view more stock data? Press y to continue:')
viewMore = input()