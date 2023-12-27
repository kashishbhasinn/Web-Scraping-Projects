#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd


# In[49]:


url = "https://en.wikipedia.org/wiki/Wikipedia:Fundraising_statistics"
tables = pd.read_html(url)


# In[50]:


type(tables)


# In[51]:


len(tables)


# In[52]:


tables[0].head()


# In[53]:


fundraising = tables[0]


# In[54]:


fundraising.head()


# In[55]:


type(fundraising)


# In[56]:


fundraising.dtypes


# In[57]:


#remove $ sign as data can be easily dealt w as an int/ a float
fundraising['Rev'] = fundraising['Revenue'].str[2:]


# In[58]:


fundraising.head()


# In[59]:


#Rev is still an object
fundraising.dtypes


# In[60]:


fundraising['Rev'] = fundraising['Rev'].str.replace(',','' )


# In[61]:


fundraising.head()


# In[62]:


#Rev still an object
fundraising.dtypes


# In[63]:


#Rev converted to an int dt
fundraising['Rev'] = pd.to_numeric(fundraising['Rev'])


# In[64]:


fundraising.head()


# In[65]:


fundraising.dtypes


# In[66]:


fundraising['Exp'] = fundraising['Expenses'].str[2:]
fundraising['Exp'] = fundraising['Exp'].str.replace(',','')


# In[67]:


fundraising.head()


# In[68]:


#All data is not always good data for eg 
fundraising.loc[0,'Exp'] = 'spam'


# In[69]:


fundraising.head()


# In[70]:


#If errors raised, we use coerce
fundraising['Exp'] = pd.to_numeric(fundraising['Exp'], errors= 'coerce')


# In[71]:


fundraising.head()


# In[72]:


fundraising.dtypes


# In[73]:


fundraising.to_csv("Fundraising.csv")

