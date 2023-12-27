#!/usr/bin/env python
# coding: utf-8

# In[40]:


import requests


# In[41]:


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r)


# In[42]:


from bs4 import BeautifulSoup 


# In[43]:


soup = BeautifulSoup(r.text, "lxml")
print(soup)


# In[44]:


boxes = soup.find_all("div", class_ ="col-md-4 col-xl-4 col-lg-4")


# In[45]:


print(boxes)


# In[46]:


print(len(boxes))


# In[47]:


names = soup.find_all("a", class_ = "title")
print(names)


# In[48]:


for i in names:
    print(i.text)


# In[49]:


price = soup.find_all("h4", class_ = "float-end price card-title pull-right")
print(price)


# In[50]:


for i in price:
    print(i.text)


# In[51]:


reviews = soup.find_all("p", class_ = "float-end review-count")
print(reviews)


# In[52]:


for i in reviews:
    print(i.text)


# In[53]:


ratings = soup.find_all("div", class_ = "ratings")
print(ratings)


# In[54]:


for i in ratings:
    print(i.text.strip())

