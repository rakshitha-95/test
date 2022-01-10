#to retrieve only single digits from a string
import re
str='one two three four five six seven 8 9 10'
result=re.findall(r'\b\d\b',str)
print(result)