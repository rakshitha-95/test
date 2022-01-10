#retrieve the phone number of a person
import re
str='Rakshitha r:8197205824'
res=re.search(r'\d+',str)
print(res.group())