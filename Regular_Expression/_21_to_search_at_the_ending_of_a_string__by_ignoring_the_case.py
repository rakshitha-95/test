#to search at the ending of a string by ignoring the case
import re
str="Hello World"
res=re.search(r"world$",str,re.IGNORECASE)
if res:
    print("strings ends with 'world'")
else:
    print("string does not end with 'world'")
