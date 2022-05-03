

# # LAB 1
# # Assignment 1
# # Name - Sunil Bhenspaliya
# # Roll. - 201951157

# In[31]:

import numpy as np
import pandas as pd
import json
from PIL import Image


# # Read csv file

# In[32]:


data = pd.read_csv('C:\\Users\\Sunilbhenspaliya\\Downloads\\district_level_service_msme.csv')


# In[33]:


print(data[0:])


# # Q1 - Create two data frames by reading above two files.

# # Create a dataframe for csv file

# In[34]:


# create dataframe for csv file

df1 = pd.DataFrame(data)


# In[35]:


print(df1)


# In[36]:


print(df1.head())


# In[37]:


print(df1.count())


# # Create Dataframe for json file

# In[38]:


filepath = 'C:\\Users\\Sunilbhenspaliya\\Downloads\\district_level_manufacturing_msme.json'
f = open(filepath)
# print(f.read)
# print(json.load(f))
data1 = json.load(f)


# In[39]:


# df2 = pd.DataFrame(data1)
print(data1['fields'])


# In[40]:


print(data1['data'])


# In[41]:


dfn = pd.DataFrame(data1['data'],columns=['STATE_NAME', 'Lg_Dist_Code', 'DISTRICT_NAME', 'MICRO', 'SMALL',
       'MEDIUM', 'Total', 'Last_Updated'])


# In[42]:


print(dfn.head())


# In[43]:


print(dfn.count())


# In[44]:


print(dfn.dtypes)


# # Q2 - Find out total ”Small” Manufacturing MSME in India.

# In[67]:


# saving dataframe json to csv file 
dfn.to_csv('dnew.csv')
# print(dfn['SMALL'])


# In[64]:


print("Total MSMS manufacturing in india is - ",dfn["SMALL"].sum())
# print(dfn["SMALL"].sum())
# print(len(df1['SMALL']))/


# In[65]:


print("State wise total manufacturing in india is ")
print(dfn.groupby("STATE_NAME").sum()["SMALL"])


# # Q3 - Create a dataframe having state wise total number of 'Micro','Small'      and "Medium" Services MSE (as shown below) and save the results as a CSV file.

# In[66]:


# print(df1.groupby("STATE_NAME")[["MICRO","SMALL","MEDIUM"]].count())
newdf = df1.groupby("STATE_NAME").sum()[["MICRO","SMALL","MEDIUM"]]
print(newdf)


# In[51]:


print(df1.head())


# In[52]:


print(df1.columns)


# 
# # Q4 - Join the both the data frame based on common STATE NAME, DISTRICT NAME, Lg Dist Code and Last Updated. The result should look like below. ”x” and ”y” in below image represent the manufacturing MSME and service MSME respectively.
# We want to merge to dataframe but before that we have to check datatype of columns we want to merge

# In[53]:


print("Data type of Dataframe1 ")
print(df1.dtypes)


# In[54]:


print("Data type of Dataframe2 ")
print(dfn.dtypes)


# Now change the datatype of dataframe to int64 as indataframe 1

# In[55]:


dfn = dfn.astype({'Lg_Dist_Code':'int64','SMALL':'int64','MEDIUM':'int64','Total':'int64','MICRO':'int64'})


# In[56]:


print("Data type of Dataframe2 ")
print(dfn.dtypes)


# In[57]:


mergedf = pd.merge(dfn,df1,on=['Lg_Dist_Code','STATE_NAME','DISTRICT_NAME','Last_Updated'])
print(mergedf)


# In[58]:


# filepath = 'C:\\Users\\Sunilbhenspaliya\\Desktop\\merge.csv'
print(mergedf.columns)


# In[59]:


mergedf.to_csv('merge.csv')


# # Q5 - Create a Pivot Table having rows STATE NAME and columns Service and Manufacturing ”MSME” as show in below. Use ”Sum” to add up district wise number.

# In[60]:


pivtable = pd.pivot_table(data=mergedf,index=['STATE_NAME'],aggfunc=np.sum)[['MEDIUM_x','MEDIUM_y','MICRO_x','MICRO_y','SMALL_x','SMALL_y']]


# In[61]:


pivtable


# In[62]:

pivtable.head()





