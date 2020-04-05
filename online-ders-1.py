#!/usr/bin/env python
# coding: utf-8

# In[23]:


import random


# In[24]:


def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers


# In[25]:


def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
        return frequency_list
            


# In[26]:


my_list=get_n_random_numbers()


# In[27]:


print(my_list)


# In[28]:


result=my_frequency_with_list_of_tuples(my_list)


# In[29]:


print(result)


# In[ ]:




