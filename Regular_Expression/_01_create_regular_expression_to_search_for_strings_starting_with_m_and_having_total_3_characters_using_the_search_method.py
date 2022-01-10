#create the reglar expression to search for strings with m and having total 3 character using the search method
import re
str="whats going on man"
result=re.search(r'm\w\w',str)
if result:#if result is not none
    print(result.group())
