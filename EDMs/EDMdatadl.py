#!/usr/bin/env python
# coding: utf-8

# In[66]:


import json
import requests
import pandas as pd
import time


# In[67]:


url = 'https://eqm-services.digiminster.com/EarlyDayMotions/list?parameters.tabledStartDate=2018-01-01&parameters.tabledEndDate=2019-01-01&parameters.orderBy=DateTabledAsc'


# In[68]:


r=requests.get(url)


# In[69]:


def getURL(url):
    print(url)
    r=requests.get(url)
    #print(r.status_code)
    return r


# In[70]:


title = []
primarysponsor = []
sponsorcount = []
date = []


# In[71]:


def loader(url):
    items = 0
    done=False
    r=getURL(url)
    count = 0
    while not done:
        count += 1     
        page = r.json()
        for i in page['Response']:
            title.append(i['Title'])
            primarysponsor.append(i['PrimarySponsor']['Name'])
            sponsorcount.append(i['SponsorsCount'])
            date.append(i['DateTabled'])
        pagelength = len(r.json())
        pageskip = count * 25
        print(len(page['Response']))
        if len(page['Response']) >= 25: 
            r=getURL(url+'&parameters.skip={}'.format(pageskip))
            time.sleep(.25)
        else: 
            done=True
    return items


# In[72]:


items = loader(url)


# In[74]:


edmdf = pd.DataFrame({'Title':title, 'Date':date, 'Primary Sponsor':primarysponsor, 'Sponsor Count':sponsorcount})


# In[75]:


edmdf


# In[76]:


edmdf.to_csv("EDMS.csv")


# In[ ]:




