#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing libraries


# In[1]:


import pandas as pd


# In[2]:


atlas = [  
    ['Франция','Париж'],  
    ['Россия','Москва'],  
    ['Китай','Пекин'],  
    ['Мексика','Мехико'],  
    ['Египет','Каир']  
] 


# In[3]:


geography = ['country', 'capital'] 


# In[4]:


world_map = pd.DataFrame(data=atlas, columns=geography) 


# In[5]:


print(world_map)


# In[6]:


movies_table = [
    ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
    ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
    ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
    ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
    ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
    ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
    ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
    ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
    ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
    ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
    ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
]

movies_filtered = [] # создаём пустой список для результатов

for movie in movies_table: # проходим по всем строкам исходной таблицы
    if movie[4] > 180: # если длительность фильма из очередной строки больше 180, 
        movies_filtered.append(movie) # то добавляем в список movies_filtered эту строку

for movie in movies_filtered: # печатаем содержимое списка списков movies_filtered
    print(movie)  


# In[13]:


import pandas as pd
df = pd.read_csv('N:\projects\data-science-time\chapter-1\chapter 1.1\music_log.csv')
# index_res = df.loc[7, 'genre']
# index_res = df.loc[:, 'genre']
index_res = df.loc[: , ['genre', 'Artist']]
# index_res = df.loc[:, 'total play': 'Artist']
# index_res = df.loc[1]
# index_res = df.loc[1:]
# index_res = df.loc[:3]
# index_res = df.loc[2:5]
print(index_res)


# In[14]:


import pandas as pd

data = [[0,0,0,0,0,0,0,0,0,0],
        [0,'-','-','-',0,0,0,0,0,0],
        [0,'-','X','-',0,0,'X','X','X','X'],
        [0,'-','X','-',0,0,0,0,0,0],
        [0,'-','-','-',0,0,0,0,0,0],
        [0,0,'-',0,0,0,0,0,'X',0],
        [0,'-','X','X',0,0,0,0,0,0],
        [0,0,'-','-',0,0,0,0,0,0],
        [0,0,0,0,'-','X',0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

columns = ['А','Б','В','Г','Д','Е','Ж','З','И','К']

battle = pd.DataFrame(data = data, columns = columns)

print(battle) 


# In[16]:


# строки датафрейма, в которых жанр — джаз (jazz)
5
jazz_df = df[df['genre'] == 'jazz']['genre'].count()
print(jazz_df)
# строки датафрейма, в которых время прослушивания total_play больше 90
high_total_play_df = df[df['total play'] > 900] 
print(high_total_play_df)
# строки датафрейма, в которых время прослушивания total_play меньше или равно 10
low_total_play_df = df[df['total play'] <= 10]
print(low_total_play_df)


# In[18]:


# сохраняем Series в отдельную переменную
total_play = df['total play']

# через логическую индексацию получаем недослушанные треки,
# и считаем их методом count()
print(total_play[total_play <= 10].count()) 


# In[35]:


# TASK - 1
pop_music = df[df['genre'] == 'pop'][df['total play'] < 10]
print(pop_music)
pop_music = df[df['genre'] == 'rock'][df['total play'] < 10]
print(pop_music)


# In[ ]:




