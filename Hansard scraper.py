
# coding: utf-8

# In[52]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib


# In[3]:


import urllib


# In[44]:


urls = ['https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True', 
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=2',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=3',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=4',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=5',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=6',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=7',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=8',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=9',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=10',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=11',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=12',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=13',
        'https://hansard.parliament.uk/search/Divisions?startDate=2015-05-03&endDate=2016-05-12&house=Commons&includeCommitteeDivisions=False&partial=True&page=14']
#scrape elements
division = []
title =[]
date = []
ayes = []
noes = []
for url in urls:
    rall = requests.get(url)
    r = rall.content
    soup = BeautifulSoup(r,"lxml")
    titles = soup.select('div.title.single-line > span')
    for t in titles:
        title.append(t.text)
    divisions = soup.select('div.division-number')
    for d in divisions: 
        division.append(d.text)
    dates = soup.select('div.information.with-portcullis.clearfix > div')
    for da in dates:
        date.append(da.text)
    ayecount = soup.select('div.counts > strong:nth-of-type(1)')
    for a in ayecount:
        ayes.append(a.text)
    nocount = soup.select('div.counts > strong:nth-of-type(2)')
    for n in nocount:
        noes.append(n.text)


# In[42]:


hansardurls = []
Speakercontrib = []
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
        #h = 'https://hansard.parliament.uk//Commons/2019-10-23/debates/2CD51EF0-690E-4E60-B520-29E93042256F/PrimeMinister'
    
    


# In[68]:


print(hansardurls)


# In[71]:


import csv
with open('hansardurls.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(hansardurls)


# In[64]:


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
    
    
    
    


# In[65]:


speakersdf = pd.DataFrame(
    {'Date': Speakingtime,
     'Speaker': Speakercontrib,
     'id': Speakerid,
     'url': urloftime
    })


# In[66]:


speakersdf


# In[49]:


votedf = pandas.DataFrame({'division':division, 'Date':date,'Vote title':title, 'Ayes':ayes, 'Noes':noes})


# In[50]:


votedf


# In[51]:


votedf.to_csv('divisions1516.csv')


# In[67]:


speakersdf.to_csv('speakerspmqdf.csv')

