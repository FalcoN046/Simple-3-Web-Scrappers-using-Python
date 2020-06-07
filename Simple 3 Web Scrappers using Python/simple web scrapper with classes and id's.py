
# coding: utf-8

# In[4]:


import requests
import bs4
l=input("enter website name : ")
c=input("enter the type of class or id name (append '.' for class name in the beginning and '#' for id name in the beginning) : ")
res=requests.get(l)
soup1=bs4.BeautifulSoup(res.text,'lxml')
soup1.select(c) 

