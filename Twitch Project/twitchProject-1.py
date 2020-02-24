#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import sqlite3 as sql
c.execute('''SELECT * FROM Chat LIMIT 20''')
# print(c.fetchall())
df_chat = DataFrame(c.fetchall(), columns=['time','device_id','login','channel','country','player','game'])
print(df_chat.head())


# In[4]:


from pandas import DataFrame


# In[5]:


connection = sql.connect('twitch.db')
c = connection.cursor()
chat = pd.read_csv(r'E:\projects\Datascience\CodeCademyProjects\Twitch Project\chat.csv')
chat.to_sql('Chat',connection,if_exists='append',index=False)
stream = pd.read_csv(r'E:\projects\Datascience\CodeCademyProjects\Twitch Project\video_play.csv')
stream.to_sql('Stream',connection,if_exists='append',index=False)


# In[6]:


print(chat.head())


# In[11]:


c.execute('''SELECT * FROM Chat
LIMIT 1''')
# print(c.fetchall())
df_chat = DataFrame(c.fetchall(), columns=['time','device_id','login','channel','country','player','game'])
print(df_chat.head())


# In[12]:


c.execute('''Select * from Stream''')
df_stream=DataFrame(c.fetchall(),columns=['time','device_id','login','channel','country','player','game','stream_format','subscriber'])
print(df_stream.head())


# In[13]:


c.execute('''SELECT Distinct game from stream''')
print(c.fetchall())


# In[14]:


c.execute('''SELECT Distinct channel from stream''')
print(c.fetchall())


# In[21]:


c.execute('''SELECT game,COUNT(*) from stream group by game ORDER BY COUNT(*) DESC''')
print(c.fetchall())


# In[22]:


c.execute('''SELECT country,COUNT(*) from stream WHERE game = 'League of Legends' group by country ORDER BY COUNT(*) DESC''')
print(c.fetchall())


# In[23]:


c.execute('''SELECT player,COUNT(*) from stream group by player ORDER BY COUNT(*) DESC''')
print(c.fetchall())


# In[24]:


c.execute('''SELECT game,
 CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY game
ORDER BY Count(*) DESC''')
print(c.fetchall())


# In[25]:


c.execute('''SELECT time
FROM stream
LIMIT 10;''')
print(c.fetchall())


# In[28]:


c.execute('''SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;''')
print(c.fetchall())


# In[31]:


c.execute('''SELECT strftime('%H', time),
   COUNT(*)
FROM stream
WHERE country = 'CA'
GROUP BY 1;''')
print(c.fetchall())


# In[33]:


c.execute('''Select * from stream inner join chat on chat.device_id = stream.device_id''')
print(c.fetchall())


# In[ ]:




