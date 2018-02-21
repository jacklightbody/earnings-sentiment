from bs4 import BeautifulSoup
import re
from selenium import webdriver
import datetime
import os
import time



def get_stock_calls(stock, min_year):
    path = "transcripts/"+stock
    if not os.path.isdir(path):
        os.mkdir(path)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    url = 'http://seekingalpha.com/symbol/'+stock+'/earnings/transcripts'
    driver.get(url)

    body_el = driver.find_element_by_tag_name("body")

    no_of_pagedowns = 50
    # load everything in the infinite scroll
    while no_of_pagedowns:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        no_of_pagedowns-=1

    elem = driver.find_element_by_xpath("//*")
    html = elem.get_attribute("outerHTML")
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    print(links)
    print(len(links))

    for link in links:
        href = link.get('href')
        try:
            if href and 'transcript' in href and 'earnings' in href:
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
                if year >= 2015: 
                    continue
                if year <= min_year:
                    return
                driver.get(transcript_url)        
                el = driver.find_element_by_xpath("//*")
                page_html = el.get_attribute("outerHTML")
                transcript_soup = BeautifulSoup(page_html, "html.parser")
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
                print(href + " done")


        except TypeError as e:
            print("Link Following Error")
            print(e)
            continue
                    


if __name__ == "__main__":
    stocks=['GOOG']#, 'BA', 'CAT', 'KO', 'BUD', 'PEP']
    min_year = 2012 


    for stock in stocks:
        get_stock_calls(stock, min_year)