#to create regular expression to extract only name but not number from a string
import re
str='Rakshitha r:8197205824'
res=re.search(r'\D+',str)
print(res.group())
