import requests
from Graphs import bar_graph, line_graph
from dotenv import load_dotenv
import os


#Function for setting up a sercure API key
def APIConfigure():
    #loads .env file
    load_dotenv()
    #sets api_key from .env file
    api_key = os.getenv("Alpha_API_key")
    return api_key


#Function for obtaining stock data
def stock_data(symbol: str, time_series: str, start_date: str, end_date: str) ->dict:
    #sets api key from .env file
    api_key = APIConfigure()
    
    #sets time series map for selection 1-4
    time_series_map={
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY", 
    }

    #sets parameters for api calls in the url so that we can keep the API key secure
    parameters={
        "function": time_series_map[time_series],
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "full"
    }

    #Base url to be modified by parameters
    url = "https://www.alphavantage.co/query"

    #reponse set equal to request
    r = requests.get(url, params=parameters)

    #data set equal to r.json for proper api calling
    data = r.json()

    #returns proper data from function
    if time_series == "1":
        key = "Time Series (5 mins)"
    elif time_series == "2":
        key = "Time Series (Daily)"
    elif time_series == "3":
        key = "Weekly Time Series"
    elif time_series == "4":
        key = "Monthly Time Series"

    time_series_data = data.get(key,{})
    filtered_data_dic = {date: values for date, values in time_series_data.items()if start_date <= date <= end_date}


    #initalizes the dic to empty 
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []

    #fills dic with data from json file
    for date, values in sorted(filtered_data_dic.items()):
        dates.append(date)
        opens.append(float(values["1. open"]))
        highs.append(float(values["2. high"]))
        lows.append(float(values["3. low"]))
        closes.append(float(values["4. close"]))
    
    print(data)
    return {"dates": dates, "open": opens, "high": highs, "low": lows, "close": closes}
        


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
    
    data = stock_data(stockSymbol, timeSeries, startDate, endDate)

    #Chart opens here
    try:
        if chartType == '1':
            title = f"Stock Data for {stockSymbol}: {startDate} to {endDate}"
            bar_graph(title, data['dates'], data['open'], data['high'], data['low'], data['close'])
        elif chartType == '2':
            title = f"Stock Data for {stockSymbol}: {startDate} to {endDate}"
            line_graph(title, data['dates'], data['open'], data['high'], data['low'], data['close'])
    except:
        print("There was an issue opening the graph.\n")

    #after chart opens

    #ask if user would like to continue
    print('Would you like to view more stock data? Press y to continue:')
    viewMore = input()