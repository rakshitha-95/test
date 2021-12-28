'''Create a dictionary  from a string'''
from collections import Counter
str1="rakshita"
mydict={}
for i in str1:
    mydict[i]=mydict.get(i,0)+1
print(mydict)