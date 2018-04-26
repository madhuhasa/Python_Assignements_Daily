# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 09:14:33 2018

@author: user
"""

# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[19]:


df=pd.read_excel("F:/assgn.xlsx")
df.head()


# In[20]:


df.corr()


# In[21]:


plt.figure(1)
plt.scatter(df['Year'],df['Population'])
plt.title("Year vs Population")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()


# In[22]:


from sklearn.cross_validation import train_test_split
X= np.array(df["Year"]).reshape(-1,1)
Y= np.array(df["Population"]).reshape(-1,1)

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3)


# In[23]:


linear = LinearRegression()
linear.fit(x_train,y_train)


# In[24]:


plt.figure(1)
plt.scatter(x_test,y_test,color='blue')
plt.plot(x_train,linear.predict(x_train),color='red')
plt.title("Year vs Population")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()


# In[28]:


f=linear.predict(2011)


# In[29]:


f


# In[30]:


f1=linear.predict(2021)
print(f1)