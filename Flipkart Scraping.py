#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[4]:


url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(url)
print(r)


# In[6]:


soup = BeautifulSoup(r.text, "lxml")
print(soup)


# In[10]:


#np = next page
np = soup.find("a", class_ = "_1LKTO3").get("href")
cnp = "https://www.flipkart.com" + np
print(cnp)


# In[12]:


# All links retrieved are either 1 or 2
# while True:
#     np = soup.find("a", class_ = "_1LKTO3").get("href")
#     cnp = "https://www.flipkart.com" + np
#     print(cnp)
#     url = cnp
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, "lxml")


# In[14]:


for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    np = soup.find("a", class_ = "_1LKTO3").get("href")
    cnp = "https://www.flipkart.com" + np
    print(cnp)


# In[15]:


Product_Name = []
Prices = []
Description = []
Reviews = []


# In[43]:


names = box.find_all("div", class_ = "_4rR01T")
print(names)


# In[48]:


Product_Names = []
for i in names:
    name = i.text.strip()
    Product_Names.append(name)


# In[49]:


print(Product_Names)


# In[50]:


len(Product_Names)


# In[51]:


prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
print(prices)


# In[52]:


Price =[]
for i in prices:
    price = i.text.strip()
    Price.append(price)


# In[53]:


print(Price)


# In[54]:


len(Price)


# In[55]:


Descriptions = []
desc = box.find_all("ul", class_ = "_1xgFaf")
for i in desc:
    description = i.text.strip()
    Descriptions.append(description)
print(Descriptions)


# In[56]:


len(Descriptions)


# In[59]:


box = soup.find("div", class_ ="_1YokD2 _3Mn1Gg")


# In[64]:


Reviews


# In[67]:


Review = Reviews[39:]


# In[68]:


len(Review)


# In[70]:


df = pd.DataFrame({"Product Names": Product_Names, "Price":Price, "Description": Descriptions, "Reviews": Review})


# In[71]:


print(df)


# In[72]:


for i in range(2,12):
        url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        box = soup.find("div", class_ ="_1YokD2 _3Mn1Gg")
        
        names = box.find_all("div", class_ = "_4rR01T")
        for i in names:
            name = i.text.strip()
            Product_Names.append(name)
        
        prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
        for i in prices:
            price = i.text.strip()
            Price.append(price)
        
        desc = box.find_all("ul", class_ = "_1xgFaf")
        for i in desc:
            description = i.text.strip()
            Descriptions.append(description)
        
        revi = box.find_all("div", class_ = "_3LWZlK")
        for i in revi:
            re = i.text.strip()
            Review.append(re)
            
df = pd.DataFrame({"Product Names": Product_Names, "Price": Price, "Description": Descriptions, "Reviews": Review})


# In[73]:


print(df)


# In[74]:


df.to_csv("Flipkart Mobiles Under 50000.csv")


# In[ ]:




