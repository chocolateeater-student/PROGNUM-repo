#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import math
a = float(input())
b= float(input())
c= float(input())
D= b**2-4*a*c
if D==0:
    x= -b/2*a
    s=f"your solutions is {x}"
elif D>0:
    x1= (-b+sqrt(D)/2*a)
    x1= (-b-sqrt(D)/2*a)
    s=f"your solutions are x1 = {x1} and x2 = {x2}"
elif D<0:
    s= rf":("

print(s)

