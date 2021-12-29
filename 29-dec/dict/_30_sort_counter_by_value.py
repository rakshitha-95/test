'''sort counter by value'''
from collections import Counter
x=Counter({'a':5,'d':123,'e':698,'f':968,'g':2})
sorted(x.items())

[(l,k) for k,l in sorted([(j,i) for i,j in x.items()])]
print(x)
[(l,k) for k,l in sorted([(j,i) for i,j in x.items()],reverse=True)]
print(x)
