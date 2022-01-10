#create the reglar expression to search for strings with m and having total 3 character using the findall() method
import re
str='man sun mop run'
result=re.findall(r'm\w\w',str)
print(result)