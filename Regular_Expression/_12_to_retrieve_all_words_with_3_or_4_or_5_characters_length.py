import re
str='one two three four five six seven 8 9 10'
result=re.findall(r'\b\w{3,5}\b',str)
print(result)