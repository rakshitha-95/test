'''Find the highest 3 values in dictionary'''
from collections import Counter
dict1={'a':1,'b':3,'c':4,'d':5,'u':7}
k=Counter(dict1)
high=k.most_common(3)
print("Dictionary with 3 higest values:")
print("keys:values")
for i in high:
    print(i[0],":",i[1]," ")
