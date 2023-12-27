#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[2]:


url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
print(r)


# In[3]:


soup = BeautifulSoup(r.text, "lxml")
print(soup)


# In[4]:


table = soup.find("table", class_="ih-td-tab auction-tbl")
print(table)


# In[5]:


title=table.find_all("th")
print(title)


# In[6]:


len(title)


# In[7]:


header=[]
for i in title:
    name = i.text
    header.append(name)
print(header)


# In[8]:


df = pd.DataFrame(columns=header)


# In[9]:


print(df)


# In[10]:


row = table.find_all("tr")
print(row)


# In[11]:


for i in row[1:]:
    data = i.find_all("td")
    r = [tr.text.strip() for tr in data]
    print(r)
    l = len(df)
    df.loc[l] = r


# In[12]:


print(df)


# In[13]:


df.to_csv("IPL Auction Stats 2022.csv")

