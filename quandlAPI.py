import requests
import json
import pprint
import datetime

queryURL = "https://www.quandl.com/api/v3/datasets/WIKI/"
APIkey = "jw6K62rHapnUJkLrCNC4"
queryParameters = {'api_key': APIkey}

def getCompanyStockData(symbol, query_date):
    r = requests.get(queryURL + symbol + ".json", params = queryParameters)
    j = json.loads(r.text)
    stockdata  = j['dataset']['data']

    currentDate = datetime.date.today()
    queryDate = datetime.date(int(query_date.split("-")[0]), int(query_date.split("-")[1]), int(query_date.split("-")[2]))
    difference = int(((4/7) * (currentDate - queryDate)).days)

    openPrice, closePrice, low, high = 0,0,0,0
    for i in range(difference, len(stockdata)):
        if stockdata[i][0] == query_date:
            openPrice, closePrice, low, high = stockdata[i][1:5]

    return [openPrice, closePrice, low, high]


def main():
    pprint.pprint(getCompanyStockData("AAPL", "2016-02-26"))

if __name__ == "__main__":
    main()
