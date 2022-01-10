import re
str='this;is the;"core" pythons\'s book'
result=re.split(r'\w+',str)
print(result)