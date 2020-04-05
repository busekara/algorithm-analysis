
# coding: utf-8

# In[2]:

list_1=[0,1,2,5]


# In[3]:

list_1[1]=10
list_1


# In[4]:

list_1[10]=10


# In[8]:

def check_prime(n):
    s=0
    if n!=1:
        for factor in range(2,n):
            s=s+1
            if n%factor==0:
                return False,s
    else:
        return False,s
    return True,s


# In[12]:

numbers=[10,13,23,310,49]
for num_ in numbers:
    print(num_,check_prime(num_))


# In[16]:

def my_search(numbers,x):
    s=0
    for i in numbers:
        s=s+1
        if i==x:
            return True,s
    return False,s


# In[18]:

numbers=[10,13,23,310,49]
x=310
my_search(numbers,x)


# In[27]:

import random


# In[28]:

def get_my_list(s):
    list_1=[]
    for i in range(s):
        t=random.randint(-100,100)
        list_1.append(t)
    return list_1


# In[31]:

def get_my_number():
    return random.randint(-100,100)


# In[32]:

my_list=get_my_list(10)
my_number=get_my_number()


# In[33]:

my_list


# In[34]:

my_number


# In[36]:

my_search(my_list,my_number)[1]


# In[48]:

my_list=get_my_list(10)
my_search_numbers=get_my_list(3)


print(" LİSTE BOYUTU : ",len(my_list))
my_search_numbers=[2,45,78,-34,55]
t=0
for x in my_search_numbers:
    t_1=my_search(my_list,x)[1]
    t=t+t_1
a,b=t,t/len(my_search_numbers)
print("ortalama deger:",b)


# In[ ]:



