from bs4 import BeautifulSoup
import re
import time
import csv
import pandas as pd
import requests
from collections import Counter
import datetime



def get_stock_calls(stock, min_year):
    transcripts = []
    url = 'http://seekingalpha.com/symbol/'+stock+'/earnings/transcripts'
    headers = {'User-Agent':'Mozilla/5.0'}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        try:
            if 'transcript' in href and 'article' in href:
                transcript_url='http://seekingalpha.com/'+href+'?part=single'
                date = link.find_next('div', {'class': 'date_on_by'}).text
                date = date.split("•")[0]
                try:
                    datetime_object = datetime.strptime(date, '%b. %-d, %Y')
                    year = datetime_object.year
                except:
                    year = datetime.datetime.now().year
                if year <= min_year:
                    print(date)
                    return
                call = requests.get(transcript_url, headers = headers)         
                transcript_soup = BeautifulSoup(call.text, "html.parser")
                try:
                    print(transcript_soup.find(id="a-cont").text)
                except:
                    continue


        except TypeError as e:
            print(e)
            continue
                    


if __name__ == "__main__":
    stocks=['AAPL']#, 'GOOG', 'BA', 'CAT', 'KO', 'BUD', 'PEP']
    min_year = 2012 

    df = pd.DataFrame(columns=['ticker','word','count'])    

    for stock in stocks:
        get_stock_calls(stock, min_year)