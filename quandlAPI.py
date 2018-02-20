import requests
import json
import pprint

queryURL = "https://www.quandl.com/api/v3/datasets/WIKI/"

def getCompanyStockData(symbol):
    r = requests.get(queryURL + symbol + ".json")
    j = json.loads(r.text)
    return j


def main():
    pprint.pprint(getCompanyStockData("AAPL"))

if __name__ == "__main__":
    main()
