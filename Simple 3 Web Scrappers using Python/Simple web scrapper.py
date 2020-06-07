
# coding: utf-8

# In[1]:


import requests
import bs4
l=input("enter website name : ") 
res=requests.get(l)
res.text
soup = bs4.BeautifulSoup(res.text,'lxml')
one=soup.select('title')
one[0].getText()

