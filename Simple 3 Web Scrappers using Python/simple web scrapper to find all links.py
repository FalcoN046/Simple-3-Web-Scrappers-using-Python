
# coding: utf-8

# In[3]:


import requests
import bs4
l=input("enter website name : ")
res=requests.get(l)
soup=bs4.BeautifulSoup(res.text,'lxml')
for link in soup.find_all('a',href=True):
    print(link['href'])

