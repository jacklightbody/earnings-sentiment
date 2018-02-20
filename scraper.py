from bs4 import BeautifulSoup
import re
import requests
import datetime
import os
import time



def get_stock_calls(stock, min_year):
    path = "transcripts/"+stock
    if not os.path.isdir(path):
        os.mkdir(path)
    url = 'http://seekingalpha.com/symbol/'+stock+'/earnings/transcripts'
    headers = {'User-Agent':'"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4)"'}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        try:
            if href and 'transcript' in href and 'article' in href:
                transcript_url='http://seekingalpha.com/'+href+'?part=single'
                date = link.find_next('div', {'class': 'date_on_by'}).text
                date = date.split("•")[0]
                try:
                    #First possible format- Sep. 7, 2017
                    datetime_object = datetime.datetime.strptime(date, '%b. %d, %Y')
                    
                except:
                    try: 
                        # for short month names SA doesn't always abbreviate ex May 4 2017
                        datetime_object = datetime.datetime.strptime(date, '%b %d, %Y')
                    except:
                        # Posts from current year don't have a year, so just add it in
                        cur_year = datetime.datetime.now().year
                        datetime_object = datetime.datetime.strptime(date+" "+str(cur_year), '%a, %b. %d %Y')

                year = datetime_object.year
                if year <= min_year:
                    print(date)
                    return
                call = requests.get(transcript_url, headers = headers)         
                transcript_soup = BeautifulSoup(call.text, "html.parser")
                try:
                    text = transcript_soup.find(id="a-cont").text
                    cleaned_text = text.split("Copyright policy:")[0]
                    file_name = datetime_object.strftime("%m_%d_%Y.txt")
                    f = open(path+"/"+file_name, 'w')
                    f.write(cleaned_text)
                    f.close()
                except Exception as e:
                    print("Transcript Parsing Error")
                    print(transcript_soup.text)
                    continue


        except TypeError as e:
            print("Link Following Error")
            print(e)
            continue
                    


if __name__ == "__main__":
    stocks=['AAPL']#, 'GOOG', 'BA', 'CAT', 'KO', 'BUD', 'PEP']
    min_year = 2012 


    for stock in stocks:
        get_stock_calls(stock, min_year)