#to find all words starting with 'an' or'ak'.
import re
str='anil akhil arun arati arundathi abhijit ankur'
res =re.findall(r'a[nk][\w]*',str)
print(res)