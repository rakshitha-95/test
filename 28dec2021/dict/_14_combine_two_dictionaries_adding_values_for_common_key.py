'''combine two dictionary adding values for common key'''
from collections import Counter
dict1={'a':45,'b':85,'c':89,'d':89}
dict2={'e':45,'b':85,'c':89,'f':89}
dict3=Counter(dict1) + Counter(dict2)
print(dict3)