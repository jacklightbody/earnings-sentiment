import pickle
from pprint import pprint
import requests
import json

#low, high, open, close

sentimentDict = pickle.load(open('sentimentDict.p', 'rb'))

def getCompanyStockData(symbol):
    queryURL = "https://www.quandl.com/api/v3/datasets/WIKI/"
    APIkey = "jw6K62rHapnUJkLrCNC4"
    queryParameters = {'api_key': APIkey}

    r = requests.get(queryURL + symbol + ".json", params = queryParameters)
    j = json.loads(r.text)
    stockdata  = j['dataset']['data']

    return stockdata

def genStockData():
    stockData = {}
    for company in sentimentDict:
        print(company)
        try:
            stockData[company] = getCompanyStockData(company)
        except KeyError:
            print("FF")

    pickle.dump(stockData, open('stockData.p', 'wb'))


def formatSystemData():
    stockData = pickle.load(open('stockData.p', 'rb'))
    pprint(stockData)

def main():
    # print(getCompanyStockData("BUD"))
    formatSystemData()

if __name__ == "__main__":
    main()
