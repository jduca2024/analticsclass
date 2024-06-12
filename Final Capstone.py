#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np



# In[2]:


df=pd.read_csv(r"C:\Users\jduca\Downloads\DOHMH_New_York_City_Restaurant_Inspection_Results_20240513.csv")


# # This step was to minimize the data to a 4 year period and then we cleaned the data to remove violation codes that were true violations. The code would really signify the business reopening, or a code would convey that no violation was found. These were removed.

# In[3]:


df_Boro = df[df['BORO'].isin(['Queens','Brooklyn'])]

start_date = '2020-01-01'

df_Boro['INSPECTION DATE'] = pd.to_datetime(df_Boro['INSPECTION DATE'])

df_Boro2 = df_Boro[(df_Boro['INSPECTION DATE'] >= start_date)]

df_Boro3 =df_Boro2[~df_Boro2['VIOLATION CODE'].isin(['28-03','20-01','06D','06F','08C','09C','20-04','20-08','10A','06B','09A','19-10','22F','09E','20D','19-06','02G','10H','04H','19-05','18-11','10D','28-06','08B','06E','28-05','Null','28-01','18G','20A'])]


# # Exported the data to ensure that the data was cleaned as expected, which it was.

# In[4]:


df_Boro3.to_csv('df_Boro3.csv', index=False)


# In[5]:


df_Boro3.groupby(['BORO'])['INSPECTION DATE'].count().reset_index()


# # Below, I created visuals for citations in Brooklyn and Queens for overall citations by year. Then overlayed the data to show the disparity and trends for each borough. Brooklyn is highest but trends down. 

# In[6]:


data = {
    "INSPECTION DATE": ['2020', '2021', '2022', '2023', '2024'],
    "BROOKLYN": [729, 4416, 16597, 15774, 6444]}

df = pd.DataFrame(data)

plt.plot(df["INSPECTION DATE"], df["BROOKLYN"], color="Green", marker="o")
plt.title("BROOKLYN INSPECTIONS BY YEAR", fontsize=14)
plt.xlabel("Years", fontsize=14)
plt.ylabel("Number of Brooklyn Inspections", fontsize=14)
plt.grid(True)
plt.show()


# In[7]:


data = {
    "INSPECTION DATE": ['2020', '2021', '2022', '2023', '2024'],
    "QUEENS": [768, 3614, 13499, 14025, 5296]}

df = pd.DataFrame(data)

plt.plot(df["INSPECTION DATE"], df["QUEENS"], color="Blue", marker="o")
plt.title("QUEENS INSPECTIONS BY YEAR", fontsize=14)
plt.xlabel("Years", fontsize=14)
plt.ylabel("Number of Queens Inspections", fontsize=14)
plt.grid(True)
plt.show()


# In[8]:


x = ['2020', '2021', '2022', '2023', '2024']
y1 = [768, 3614, 13499, 14035, 5296]
y2 = [729, 4416, 16597, 15774, 6444]

plt.plot(x, y1, label ='Queens')
plt.plot(x, y2, '-.', label ='Brooklyn')

plt.xlabel("Years")
plt.ylabel("Number of Inspections")
plt.legend()
plt.title('Brooklyn vs Queens Inspection Overlay')
plt.show()


# # Additional Analysis on citations by the types critical citation by borough. Brooklyn is still higher in critical citations overall. This was charted as well to show the cumulative numbers for critical citations. 

# In[9]:


df_Boro3.groupby(['BORO','CRITICAL FLAG'])['INSPECTION DATE'].count().reset_index()
                            


# In[10]:


import matplotlib.pyplot as plt
import numpy as np

# Defining categories and their corresponding values for two groups
Categories = ['Critical', 'Not Applicable', 'Not Critical']
Brooklyn = [22521, 533, 20906]
Queens = [18956, 504, 17752]

# Setting the width of the bars 
bar_width = 0.35
# Calculating bar positions for both groups
bar_positions1 = np.arange(len(Categories))
bar_positions2 = bar_positions1 + bar_width

# Creating the first set of bars (Group 1)
plt.bar(bar_positions1, Brooklyn, width=bar_width, label='Brooklyn', color='skyblue')
# Create the second set of bars (Group 2) next to the first set
plt.bar(bar_positions2, Queens, width=bar_width, label='Queens', color='orange')

# Adding labels to the axes
plt.xlabel('Critical Citation')
plt.ylabel('Volume of Critical Citations')

x_pos = np.arange(len(Categories))
plt.xticks(x_pos, Categories, color='black')
plt.yticks(color='black')


# Adding a title to the graph
plt.title('2020-2024 Cumulative Critical Citations')
plt.legend()
plt.show()


# # I did one last observation by cuisine.  Additional analysis shows that american food in Brooklyn trends highest for citations, followed by Chinese food in Queens and Chinese food in Brooklyn. 

# In[11]:


df_brooklyncuisine = df_Boro2.groupby(['BORO','CUISINE DESCRIPTION'])['INSPECTION DATE'].count().reset_index()
df_brooklyncuisine = df_brooklyncuisine.sort_values('INSPECTION DATE', ascending=False)
df_brooklyncuisine.head(10)


# In[12]:


import matplotlib.pyplot as plt
import numpy as np

# Defining categories and their corresponding values for two groups
Categories = ['American Cuisine', 'Chinese Cuisine', 'Pizza']
Brooklyn = [7969, 6440, 3787]
Queens = [6003, 7083, 2920]

# Setting the width of the bars 
bar_width = 0.35
# Calculating bar positions for both groups
bar_positions1 = np.arange(len(Categories))
bar_positions2 = bar_positions1 + bar_width

# Creating the first set of bars (Group 1)
plt.bar(bar_positions1, Brooklyn, width=bar_width, label='Brooklyn', color='teal')
# Create the second set of bars (Group 2) next to the first set
plt.bar(bar_positions2, Queens, width=bar_width, label='Queens', color='purple')

# Adding labels to the axes
plt.xlabel('')
plt.ylabel('Count of Citation')

x_pos = np.arange(len(Categories))
plt.xticks(x_pos, Categories, color='black')
plt.yticks(color='black')


# Adding a title to the graph
plt.title('Citations by Cuisine')
plt.legend()
plt.show()


# # In conclusion, Brooklyn is higher in both overall citations and critical citations than queens. Numbers were impacted by covid early in the dataset. Brooklyn is showing a downward trend over the 4 year period and queens is showing an upward trend.  

# In[ ]:




