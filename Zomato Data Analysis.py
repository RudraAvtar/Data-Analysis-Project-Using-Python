#!/usr/bin/env python
# coding: utf-8

# # Import necessary Python libraries.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())


# In[5]:


dataframe = pd.read_csv("Zomato data .csv")


# In[6]:


dataframe


# # Let's convert the data type of the "rate" column to float and remove the denominator

# In[7]:


def handelRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handelRate)
print(dataframe.head())


# In[8]:


dataframe.info()


# # CONCLUSION: There is no NULL valur in dataframe

# # Type of Restaurant

# In[10]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of Restaurant")


# # CONCLUSION: The majority of the restaurants fall into the dining category

# # Dining restaurants are preferred by a lareger number of individuals.

# In[11]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green",marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)


# # The majority of restaurants received ratings
# 

# In[12]:


plt.hist(dataframe['rate'],bins=5)
plt.title("Ratings Distribution")
plt.show()


# # Conclusion:The majoruty of restaurants received ratings from 3.5 to 4
# 

# # The majority of couplees prefer restaurants with an approximate cost of 300 rupees.

# In[13]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # Whether online orders receive higher rating than offline orders.

# In[16]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)


# # CONVLUSION: Offline orders received lower rating comparison to online orders, which obtained excellent ratings.

# In[17]:


pivot_table = dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu",fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# # CONCLUSION: Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. This suggests that clients prefer to place orders in person at restaurants,but prefer online ordering at cafes.
