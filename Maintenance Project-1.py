#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("maintenance_data.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[6]:


df.describe()


# # Conclusion
# 
# 1.Avg Lifetime of Machine is around 55 year
# 2.25% of machine having age of 34 year,50% having age of 60 year & 75 % of machine having age of 80 year.Max age is 93.
# 3.Avg Pressure borne by a Machine is around 98.
# 4.25% of machine had pressure around 85,50% had pressure around 97 & 75 % of machine had pressure around 112.Max pressure is 173
# 5.Avg Moisture borne by a Machine is around 99.
# 6.25% of machine had Moisture around 92,50% had Moisture around 99 & 75 % of machine had Moisture around 106.Max Moisture is 128
# 7.Avg Temp borne by a Machine is around 100.
# 8.25% of machine had Temp around 87,50% had Temp around 100 & 75 % of machine had Temp around 113.Max Temp is 172

# In[19]:


con=["lifetime","pressureInd","moistureInd","temperatureInd"]
cat=["broken","team","provider"]


# In[20]:


df=df.drop_duplicates()


# In[22]:


df.shape


# ### No Duplicate value found

# In[23]:


df.isnull().sum()


# ### No Null value found

# In[24]:


for i in cat:
    sns.countplot(x=i,data=df)
    plt.show()


# ### Conclusion:
# 1.Provider 2 is the most machine provider with number of >250. The rest consist of Provider 3 and 4 (<200), and Provider 1 (250).

# In[26]:


out=pd.crosstab(df["provider"],df["broken"],margins=True)


# In[27]:


out


# ### Conclusion:
# 1.Provider 2 is the most machine provider
# 2.Out of 266 machines only 91 are damaged.34% non operating.
# 3.Provider 1 has most damaged machine i.e 116 out of 254.45% non operating.
# 4.Provider 3 has 114 damaged machine out of 242.47% non operating.
# 5.Provider 4 has 76 damaged machine out of 238.47% non operating.32% non operating.

# In[28]:


for i in con:
    sns.scatterplot(x=df.index, y=df[i])
    plt.show()


# ### Conclusion:
# 1.As we can se at this scattering graph, most of the dots (which signify the machines) gathering at 60-80. From this data we can conclude that majority of the machines have durable quality that could be proven by how long the machine have operated until they taking damage.
# 2.In order for a machine to keep operating until they reach age of 60-80, they have to be operated in temperature that ranged from 60-120. Not many machine able to work under temperature of 140 or 160, so this should be taken as factor of consideration
# 3.In order for a machine to keep operating until they reach age of 60-80, they have to be operated in pressure that ranged from 60-120. Not many machine able to work under pressure of 140 or 160, so this should be taken as factor of consideration
# 

# In[30]:


sns.scatterplot(x="provider",y="lifetime",hue="broken",data=df)
plt.show()


# ### Conclusion:
# Not only the percentage of damaged numbers, Provider 2 also good at durability aspect.

# In[32]:


out1=pd.crosstab(df["team"],df["broken"],margins=True)
out1


# ### Conclusion:
# Team B become most user of machines with the number of 356. The number of machine that they have now is 206, while 205 of them already non operated. Team A operate
# machine as many as 336 while damage 123 of them. Team C operate 308 machine while damage 124 of them.

# In[35]:


sns.scatterplot(x="moistureInd",y="temperatureInd",hue="broken",data=df)
plt.show()


# In[36]:


sns.heatmap(df.corr(),annot=True,cmap="coolwarm")


# ### Conclusion:
#   Positive correlation (0<x<1) in this founding consist of :
# - Moisture and lifetime (0,24), the more moisture increase, the lifetime also follow
# - Moisture and broken (0,34), the more moisture increase, the probability of machine got damage also increase
# - Lifetime and broken (0,2) the more lifetime increase, the probability of broken also increase
# - Temperature and broken (0,7) the more temperature increase, the probability of broken also increase.
