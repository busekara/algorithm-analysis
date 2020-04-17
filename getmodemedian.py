#!/usr/bin/env python
# coding: utf-8

# In[1]:


def getModeMedian(list_1):
    n = len(list_1) #1
    for i in range(n): #bütün for döngüsünün karmaşıklığı:n*n=n^2

        for j in range(0, n-i-1):
 
            if list_1[j] > list_1[j+1] :
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
    if(n%2==0):#3 
        a=int(n/2)-1 #3
        b=int(n/2)   #2
        median=(list_1[a]+list_1[b])/2 #3
        
    else:
        c=int((n)/2) #2
        median=list_1[c]  #1
    counts = {} #1
    for item in list_1: #n*n=n^2
        counts [item] = counts.get (item, 0) + 1 #2
        maxcount = 0 #1
        maxitem = None  #1
        for k, v in counts.items ():  #n
            if v > maxcount:
                maxitem = k
                maxcount = v
    mode=maxitem #1
    
    return median,mode
#toplam karmaşıklık= n^2


# In[2]:


getModeMedian([10, 6, 2, 6])





