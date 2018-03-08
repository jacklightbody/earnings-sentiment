from bs4 import BeautifulSoup
import re
from selenium import webdriver
import datetime
import os
import time
import requests
import json



def get_stock_calls(stock, min_year):
    path = "transcripts/"+stock
    if not os.path.isdir(path):
        os.mkdir(path)

    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    page = 0

    done = False
    url = 'http://seekingalpha.com/symbol/'+stock+'/earnings/more_transcripts?page='
    html = '<html>'
    while not done:
        driver.get(url+str(page))
        el = driver.find_element_by_xpath("//*")
        page_html = el.text
        print(page_html)
        response = json.loads(page_html)
        if len(response['html']) < 2:
            done = True
        html = html + response['html'] 
        page += 1
    html += '</html>'

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    hrefs = set()
    deduped_links = []
    for link in links:
        if link.get('href') not in hrefs:
            deduped_links.append(link)
            hrefs.add(link.get('href'))

    for link in deduped_links:
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

                if year <= min_year:
                    return
                driver.get(transcript_url)        
                el = driver.find_element_by_xpath("//*")
                page_html = el.get_attribute("outerHTML")
                content = ''
                try:
                    content = extract_transcript(page_html)
                
                except Exception as e:
                    print("Transcript Parsing Error")
                    # give us time to manually do the captcha and then try again
                    time.sleep(20)
                    try: 
                        content = extract_transcript(page_html)
                    except:
                        # if it fails twice then just skip it, probably mal-formed for some reason
                        continue
                file_name = datetime_object.strftime("%m_%d_%Y.txt")
                f = open(path+"/"+file_name, 'w')
                f.write(content)
                f.close()
                print(href + " done")
                time.sleep(5)


        except TypeError as e:
            print("Link Following Error")
            print(e)
            continue
                    
def extract_transcript(page_html):
    transcript_soup = BeautifulSoup(page_html, "html.parser")
    text = transcript_soup.find(id="a-cont").text
    cleaned_text = text.split("Copyright policy:")[0]
    return cleaned_text

if __name__ == "__main__":
    stocks=['CA']#, 'BA', 'CAT', 'KO', 'BUD', 'PEP']
    min_year = 2012 


    for stock in stocks:
        get_stock_calls(stock, min_year)