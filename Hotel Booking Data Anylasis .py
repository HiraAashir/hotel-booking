#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[4]:


df = pd.read_csv('hotel_booking.csv')


# In[5]:


df.head(10)


# In[6]:


df.tail()


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df.info()


# In[12]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[13]:


df.info()


# In[14]:


df.describe(include = 'object')


# In[16]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[17]:


df.isnull().sum()


# In[34]:


df.isnull().sum()


# In[38]:


df.describe()


# In[36]:


df['adr'].plot(kind = 'box')


# In[37]:


df = df[df['adr'] <5000]


# In[46]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5, 4))
plt.title('Reservation status count')
plt.bar(['Not Canceled', 'Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()
plt.figure(figsize = (5, 3))
plt.title('previous_cancellations')
plt.bar(['Not Canceled', 'Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()
plt.figure(figsize = (7, 5))
plt.title('total_of_special_requests')
plt.bar(['Not Canceled', 'Canceled'],df['is_canceled'].value_counts(), edgecolor = 'red', width = 0.7)
plt.show()
plt.figure(figsize = (7, 5))
plt.title('customer type')
plt.bar(['Transient', 'Contract'],df['is_canceled'].value_counts(), edgecolor = 'green', width = 0.7)
plt.show()


# In[54]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df)
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1, 1))
plt.title('Reservation status in different hotels', size=20)
plt.xlabel('Hotel')
plt.ylabel('Number of reservations')
plt.show()


# In[55]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[57]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[60]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()

plt.figure(figsize = (20, 8))
plt.title('Average daily rate in city and resort hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[62]:


df['Hotel'] = df['reservation_status_date'].dt.month

plt.figure(figsize=(16, 8))
ax1 = sns.countplot(x='Hotel', hue='is_canceled', data=df, palette='bright')
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1, 1))
plt.title('Reservation status per month', size=20)
plt.xlabel('Month')
plt.ylabel('Number of reservations')
plt.legend(['Not Canceled', 'Canceled'])
plt.show()


# In[69]:


import matplotlib.pyplot as plt
import seaborn as sns

df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize=(15, 8))
plt.title('ADR per month', fontsize=30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')['adr'].sum().reset_index())
plt.xlabel('Month')
plt.ylabel('ADR')
plt.show()


# In[75]:


canceled_data = df[df['is_canceled'] == 1]
top_7_country = canceled_data['country'].value_counts()[:7]
plt.figure(figsize = (7, 7))
plt.title('Top  countries with reservation canceled')
plt.pie(top_7_country, autopct = '%.2f', labels = top_7_country.index)
plt.show()


# In[76]:


df['market_segment'].value_counts()


# In[77]:


df['market_segment'].value_counts(normalize = True)


# In[78]:


canceled_data['market_segment'].value_counts(normalize = True)


# In[79]:


canceled_df_adr = canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace = True)
canceled_df_adr.sort_values('reservation_status_date', inplace = True)

not_canceled_data = df[df['is_canceled'] == 0]
not_canceled_df_adr = not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace = True)
not_canceled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20, 8))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label = 'not canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend()


# In[87]:


canceled_df_adr = canceled_df_adr[(canceled_df_adr['reservation_status_date']>'2016') & (canceled_df_adr['reservation_status_date']< '2017-09')]
not_canceled_df_adr = not_canceled_df_adr[(not_canceled_df_adr['reservation_status_date']>'2016') & (not_canceled_df_adr['reservation_status_date']< '2017-09')]

plt.figure(figsize = (20, 9))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label = 'not canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend(fontsize = 20)
plt.show()


# In[ ]:




