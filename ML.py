import pickle
from pprint import pprint
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#open, high, low, close

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
            continue

    pickle.dump(stockData, open('stockData.p', 'wb'))


def formatSystemData():
    del sentimentDict["BUD"]

    stockData = pickle.load(open('stockData.p', 'rb'))
    dateStockData = {}
    for company in sentimentDict:
        dateStockData[company] = {}
        companyStockData = stockData[company]

        for date in sentimentDict[company]:
            month, day, year = date.split("_")
            quandlDateFormat = year + "-" + month + "-" + day

            for i, day in enumerate(companyStockData):
                if day[0] == quandlDateFormat:
                    dateStockData[company][date] = [day[1:5]]
                    dateStockData[company][date].append(companyStockData[i+1][1:5])
                    dateStockData[company][date].append(companyStockData[i+2][1:5])
                    dateStockData[company][date].append(companyStockData[i+3][1:5])
                    dateStockData[company][date].append(companyStockData[i+4][1:5])
                    dateStockData[company][date].append(companyStockData[i+5][1:5])

    pairs = []
    for company in sentimentDict:
        for date in sentimentDict[company]:
            callDayOpen, nextDayClose = dateStockData[company][date][0][0], dateStockData[company][date][1][0]
            twoDayPctChange = (nextDayClose - callDayOpen)/callDayOpen

            execSum = 0
            for executive in list(sentimentDict[company][date].keys()):
                execSum += sentimentDict[company][date][executive]

            execAvg = execSum / len(list(sentimentDict[company][date].keys()))
            pairs.append([execAvg, twoDayPctChange, company])

    return pairs

def main():
    # print(getCompanyStockData("AAPL"))
    pairs = formatSystemData()
    pairsDF = pd.DataFrame(pairs)
    pairsDF.columns = ["sentimentAvg", "twoDayPctChange", "company"]

    sns.lmplot(x = "sentimentAvg", y = "twoDayPctChange", data = pairsDF, fit_reg=False, hue="company", legend=False)
    plt.xlabel("Sentiment Average")
    plt.ylabel("Two Day Pct Change")
    plt.legend(loc='lower left')
    plt.title("Stock 2 Day Pct. Change against Sentiment Average for Earnings Call")
    plt.show()


if __name__ == "__main__":
    main()
