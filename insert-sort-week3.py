#!/usr/bin/env python
# coding: utf-8

# In[10]:


def my_insertion_sort(arr=[2,1,6,-2,4,9,-5]):
    n=len(arr)
    loop_counter=0
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            loop_counter=loop_counter+1
        arr[j+1]=key
    return arr,loop_counter
    


# In[11]:


arr=[2,1,6,-2,4,9,-5]
print(arr)


# In[12]:


arr,l_c=my_insertion_sort()
print(arr,l_c)


# In[ ]:




