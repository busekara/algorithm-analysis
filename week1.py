
# coding: utf-8

# In[5]:

def f_recursive(n):
    if n<2:
        return n
    else:
        return f_recursive(n-1)+f_recursive(n-2)
for i in range(15):
    print(i,f_recursive(i))


# In[8]:

def f_loop(n):
    if n<2:
        return n
    else:
        a=0
        b=1
        c=a+b
        s=2
        while(s<n):
            a=b
            b=c
            c=a+b
            s=s+1
        return c
for i in range(15):
    print(i,f_loop(i))


# In[ ]:



