#!/usr/bin/env python
# coding: utf-8

# In[2]:


liczba=245003
liczbastr=range(len(str(liczba)))

temp1=[]

print(liczba)


for i in liczbastr:
    temp1.append((pow(10,len(str(liczba))-i-1))*1)

print('temp1: ', temp1)    

liczbas=str(liczba)

temp2=[]
for i in liczbas:
    temp2.append(int(i))

print('temp2: ', temp2)

temp1a=[]
temp2a=[]

Result = []
for i1, i2 in zip(temp1, temp2):
    if i2!=0:
        temp1a.append(i1)
        temp2a.append(i2)
        

for i1, i2 in zip(temp1a, temp2a):
        Result.append(str(i1*i2))

print('temp1a adjusted: ', temp1a)         
print('temp2a adjusted: ', temp2a)

result2=""

print(Result)



s = ' + '.join([str(n) for n in Result])
print(s)
# 0-1-2


#Joined=''.join(str(Result))
#print(Joined)


# In[ ]:





# In[ ]:





# In[ ]:




