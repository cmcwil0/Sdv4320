import pygal
import lxml
import requests

def validDate(date):
        if len(date) != 10:
            return False
        if date[4] != '-' or date[7] != '-':
            return False
        
        year = date[:4]
        month = date[5:7]
        day = date[8:]

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False

        year = int(year)
        month = int(month)
        day = int(day)

        if not (1 <= month <= 12):
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not (1 <= day <= 31):
                return False
        elif month in [4, 6, 9, 11]:
            if not (1 <= day <= 30):
                return False
        elif month == 2:
            if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                if not (1 <= day <= 29):
                    return False
            else:
                if not (1 <= day <= 28):
                    return False

        return True

print('-------Stock Data Visualizer-------')

viewMore = 'y'

while viewMore == 'y':
    #get stock symbol
    print('Enter the stock symbol you are looking for: ')
    stockSymbol = input()

    #get an validate chart type input
    chartOptions = ['1','2']
    while True:
        print('''
Chart Types
-----------
1. Bar
2. Line
    
Enter the chart type you want (1,2): ''')
        chartType = input()
        if chartType not in chartOptions:
            print("Invalid input for chart type")
            continue
        else:
            break

    #get and validate time series option input
    timeOptions = ['1','2','3','4']
    while True:
        print('''
Select the Time Series of the chart you want to Generate
--------------------------------------------------------
1. Intraday
2. Daily
3. Weekly
4. Monthly

Enter time series option (1, 2, 3, 4):''')
        timeSeries = input()
        if timeSeries not in timeOptions:
            print("Invalid input for time series")
            continue
        else:
            break

    #get and validate start and end dates
    while True:
        print('Enter the start Date (YYYY-MM-DD): ')
        startDate = input()
        if validDate(startDate) is False:
            print("Invalid input for Start date")
            continue

        print('Enter the end Date (YYYY-MM-DD): ')
        endDate = input()
        if validDate(endDate) is False:
            print("Invalid input for End date")
            continue

        if startDate > endDate:
            print("Invalid input: Start date must be before End date")
            continue
        else:
            break

    #Chart opens here


    #after chart opens

    #ask if user would like to continue
    print('Would you like to view more stock data? Press y to continue:')
    viewMore = input()