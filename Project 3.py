#!/usr/bin/env python
# coding: utf-8

# # importing data and reviewing

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[22]:


df=pd.read_csv(r"C:\Users\jduca\OneDrive - Healthfirst\Desktop\NYPD_Arrest_Data__Year_to_Date__20240506.csv")


# In[3]:


df.head(75)


# # Getting column names and isolating Disorderly Conduct and Arson Crimes individually

# In[4]:


df.columns


# In[10]:


filtered_df = df.loc[df['OFNS_DESC'] == 'DISORDERLY CONDUCT']
filtered2_df = df.loc[df['OFNS_DESC'] == 'ARSON']


# In[6]:


filtered_df.head(500)


# # Grouping Disorderly data and graphing it 

# In[7]:


#clean/filtered data down to only disorderly conduct by Gender
Disorderly_df = filtered_df.groupby(['OFNS_DESC','PERP_SEX'])['ARREST_KEY'].count().reset_index()
print(Disorderly_df)


# In[8]:


# creating the dataset
data = {'Female Disorderly': 204, 'Male Disorderly':111}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon', 
        width = 0.4)
 
plt.xlabel("Disorderly Conduct by Gender")
plt.ylabel("Number of Arrests")
plt.title("NYC Disorderly Conduct")
plt.show()


# In[9]:


# additional Context to include borough and gender
filtered_df.groupby(['OFNS_DESC','PERP_SEX','ARREST_BORO'])['ARREST_KEY'].count().reset_index()

#Borough of arrest. B(Bronx), S(Staten Island), K(Brooklyn), M(Manhattan), Q(Queens)


# In[12]:


filtered2_df.groupby(['OFNS_DESC','PERP_SEX','ARREST_BORO'])['ARREST_KEY'].count().reset_index()

#Borough of arrest. B(Bronx), S(Staten Island), K(Brooklyn), M(Manhattan), Q(Queens)


# # Grouping Arson data by gender and boro, then just gender. Lastly,  graphing it to show disparity across boroughs.   

# In[21]:


filtered2_df.groupby(['OFNS_DESC','PERP_SEX'])['ARREST_KEY'].count().reset_index()


# In[20]:


# creating the dataset
data = {'Bronx M': 9, 'Bronx F':3,'Brooklyn M': 8, 'Brooklyn F': 2,'NYC M': 3,
        'NYC F':1,'Queens M': 5, 'Queens F':1, 'Staten M': 1}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon', 
        width = 0.6)
 
plt.xlabel("Arson by Gender")
plt.ylabel("Number of Arrests")
plt.title("NYC Arson")
plt.show()


# # Summary: I went into this project expecting men to be higher in disorderly conduct than women. This was not the case and women were almost twice as high. However, I ran an additional groupby to include borough and its mostly Manhattan (303). All other borough combined equal 12 arrests. The issue here is that its possible this is mostly tourists, or that other boroughs have not yet submitted their data for this type of crime in totality. It does seem skewed to its locality due to spike in one borough over another. I graphed the data by gender as opposed to borough only because of the low numbers via brough. 
# 
# # As a result, I did a look up of Arson to find something with some more data points and less skewed numbers. Almost 4 times as many males commit arson when compared to females. Additionally, the Bronx and Brooklyn lead the way in arson cases with Staten Island being the safest area to be when avoiding arsonists. 

# In[ ]:




