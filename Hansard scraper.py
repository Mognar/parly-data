
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

hansardurls = []
urls = ['https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=1&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=2&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=3&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=4&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=5&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=6&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=7&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=8&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=9&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=10&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=11&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=12&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=13&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=14&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=15&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=16&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=17&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=18&partial=true',
       'https://hansard.parliament.uk/search/Debates?endDate=2019-10-28&house=Commons&searchTerm=%22Prime+Minister%22&startDate=2009-06-23&page=19&partial=true',]
for url in urls:
    rall = requests.get(url)
    r = rall.content
    soup = BeautifulSoup(r,"lxml")
    titles = soup.find_all('a',class_="no-underline")
    for t in titles:
        if t['title'].lower() == "prime minister [house of commons]":
            hurl = 'https://hansard.parliament.uk/'+t['href']
            hansardurls.append(hurl)

print(hansardurls)

import csv
with open('hansardurls.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(hansardurls)

Speakercontrib = []
Speakerid = []
Speakingtime = []
urloftime = []
#h = 'https://hansard.parliament.uk//Commons/2019-10-23/debates/2CD51EF0-690E-4E60-B520-29E93042256F/PrimeMinister'
for h in hansardurls:
    rall = requests.get(h)
    r = rall.content
    soup = BeautifulSoup(r,"lxml")
    time = soup.find('div',class_="col-xs-12 debate-date").text
    contributors = soup.find_all('h2',class_="memberLink")
    for c in contributors:
        link = c.find('a')
        try:
            member = link.text
        except: 
            print(c)
        try:
            identifier = link['href']
        except: 
            pass
        if "Speaker" in member:
            Speakercontrib.append(time + " - " + member)
            Speakerid.append(identifier)
            Speakingtime.append(time)
            urloftime.append(h)


speakersdf = pd.DataFrame(
    {'Date': Speakingtime,
     'Speaker': Speakercontrib,
     'id': Speakerid,
     'url': urloftime
    })

speakersdf

speakersdf.to_csv('speakerspmqdf.csv')

