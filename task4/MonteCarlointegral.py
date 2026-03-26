#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#4.6
import numpy as np

f=input("function. NOW.")
a=int(input("first boundry. NUMBER"))
b=int(input("second boundry. NUMBER. GO."))
n=1000

x=np.random.uniform(a, b, n)
integ=((b-a)/n)*sum(eval(f))
print(integ)

