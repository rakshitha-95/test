#create the reglar expression to search for strings with m and having total 3 character using match() method
import re
str='man sun mop run'
result=re.match(r'm\w\w',str)
print(result)