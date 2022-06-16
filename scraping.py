#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[6]:


pip install bs4


# In[16]:


from bs4 import BeautifulSoup
import requests 
url='https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid'
page=requests.get(url)

page.content


# In[49]:


import pandas as pd
from bs4 import BeautifulSoup
import requests 
try:
    source = requests.get('https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid')
    source.raise_for_status()

    soup=BeautifulSoup(source.text,'html.parser')
    events=soup.find('tbody').find_all('tr')
    #print(events)
    event_id=[]
    event_name=[]
    event_date=[]
    for event in events:
        id=event.find('td').text
        name=event.find('td').find_next_siblings()[0].text
        date=event.find('td').find_next_siblings()[1].text
        #print(id,name,date)
        event_id.append(id)
        event_name.append(name)
        event_date.append(date)
    #print(event_id)
    #print(event_name)
    #print(event_date)
    
        id = event.get_text(strip=True)
    df = pd.DataFrame({'event ID': event_id, 'event name': event_name, 'event date': event_date})
    df.to_csv(r"C:\Users\HP\Desktop\event.csv", index=False)
    
    
except Exception as e:
    print(e)


# In[ ]:





# In[ ]:




