#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
from random import choice


# In[7]:


#Creating the transformations
def trans_1(p):
    x = p[0]
    y =p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1,y1

def trans_2(p):
    x = p[0]
    y =p[1]
    x1 = 0.5 + 0.5 * x
    y1 = 0.5 + 0.5 * y
    return x1,y1

def trans_3(p):
    x = p[0]
    y =p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1,y1


# In[11]:


transformation = [trans_1,trans_2,trans_3]
a1 = [0]
b1 = [0]
a,b = 0,0

for i in range(10000000):
    trans = choice(transformation)
    a,b = trans((a,b))
    a1.append(a)
    b1.append(b)
    


# In[12]:


plt.rc('figure', figsize = (20,16))


# In[13]:


plt.plot(a1,b1,'o')


# In[ ]:




