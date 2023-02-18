#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
measurements = [['Солнце',146,152], # Измерения хранятся в списке списков 
              ['Луна',0.36, 0.41], # measurements (англ. «измерения»).
              ['Меркурий',82, 217], 
              ['Венера',38, 261],
              ['Марс',56,401],
              ['Юпитер',588, 968],
              ['Сатурн',1195, 1660],
              ['Уран',2750, 3150],
              ['Нептун', 4300, 4700],
              ['Комета Галлея', 6, 5400]]

# Названия столбцов хранятся в переменной header.
header = ['Небесные тела ','MIN', 'MAX'] 

# Сохраним структуру данных в переменной celestial (англ. «небесный»).
celestial = pd.DataFrame(data=measurements, columns=header) 


# In[6]:


print(celestial.columns) 


# In[8]:


celestial = celestial.rename(columns={'Небесные тела ': 'celestial_bodies', 'MIN': 'min_distance', 'MAX': 'max_distance'}) 


# In[9]:


print(celestial.columns) 


# In[10]:


import pandas as pd
df = pd.DataFrame({
    'item': ['shirt', 'shirt', 'shirt', 'shirt', 'hat'],
    'style': ['classic', 'classic', 'casual', 'classic', 'casual'],
    'rating': [4, 4, 3.5, 4, 5]
})
print(df, '\n')
print(df.duplicated())


# In[26]:


df_1 = pd.read_csv('N:\projects\data-science-time\chapter-1\chapter 1.1\music_log.csv')
df = pd.read_csv('N:\projects\data-science-time\chapter-1\chapter 1.1\music_log_upd.csv')


# In[23]:


print(df.isna().sum())


# In[20]:


print(df_1['total play'].mean())
print(df['total_play_seconds'].mean())
# print(df_2['total play'].mean())


# In[27]:


print(df[df['total_play_seconds'] == df['total_play_seconds'].max()]) 


# In[28]:


df_drop_null = df[df['total_play_seconds'] != 0]
print(df_drop_null['total_play_seconds'].min()) 


# In[29]:


print(df_drop_null[df_drop_null['total_play_seconds'] == df_drop_null['total_play_seconds'].min()]) 


# In[30]:


df_stat_1 = df.tail()
print(df_stat_1['total_play_seconds'].sort_values()) 


# In[31]:


df_stat = df.tail(4)
print(df_stat['total_play_seconds'].sort_values()) 


# In[32]:


print(df_stat['total_play_seconds'].median()) 


# In[33]:


df_drop_null = df[df['total_play_seconds'] != 0]
print(df_drop_null['total_play_seconds'].median()) 


# In[34]:


print(df_drop_null['total_play_seconds'].mean()) 


# In[ ]:




