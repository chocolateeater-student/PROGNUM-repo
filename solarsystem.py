#!/usr/bin/env python
# coding: utf-8

# In[12]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

bigmasses= []
for i in range(len(masses)):
    if masses[i]>=masses[9]:
        bigmasses.append(masses[i])

print(bigmasses)

mass= masses[6:]
avr=sum(mass)/len(mass)
print(f"the average of the last 5 terms is {avr}")


# In[ ]:




