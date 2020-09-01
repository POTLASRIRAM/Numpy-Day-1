#!/usr/bin/env python
# coding: utf-8

# In[28]:


# cheking numpy version
import numpy as np
print(np.__version__)


# ### Numpy array creation

# In[29]:


# creating numpy ndarray object
#array()
import numpy as np
a=np.array([1,2,3,4,5])
print(a)


# In[30]:


a=np.array([[1,2,3,4],[1,2,3,4]])
print(a)


# In[31]:


a=np.array([[[1,2,3],[1,2,3]]])
print(a)


# In[2]:


# Dimensions in array
#0-D 
import numpy as np
a=np.array(42)
print(a)


# In[3]:


# 1-D
a=np.array([1,2,3,4])
print(a)


# In[5]:


## 2-D
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)


# In[6]:


# 3-D
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a)


# In[7]:


#Checking no of dimension's
a=np.array([1,2,3,4])
print(a.ndim)


# In[33]:


#Higher Dimensional array
a=np.array([1,2,3,4,5],ndmin=6)
print(a)


# ### Numpy array indexing

# In[34]:


# Access array elements
#1-D
a=np.array([1,2,3,4])
print(a[2])


# In[35]:


#2-D
a=np.array([[1,2,3],[1,2,3]])
print(a[0,1])


# In[37]:


#3-D
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a)


# In[38]:


#Negative indexing
a=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(a[1,-2])


# ### Numpy array slicing

# In[42]:


#Slicing array [start:end]
a=np.array([1,2,3,4,5])
print(a[0:5])


# In[45]:


# STEP
print(a[1:5:2])


# In[16]:


# Slicing 2-D array
a=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(a[1,1:4])


# In[17]:


print(a[0:2,2])


# In[18]:


print(a[0:2,1:4])


# ### Numpy data types

# In[19]:


# int,bool,string,float


# In[20]:


#Checking data types
a=np.array([1,2,3])
print(a.dtype)


# In[21]:


#Creating Data type with defined Data type
a=np.array([1,2,3,4],dtype='i')
print(a.dtype)


# In[22]:


#Converting dtype on existing array's
a=np.array([1.1,2.1,3.1])
b=a.astype('i')
print(b.dtype)



