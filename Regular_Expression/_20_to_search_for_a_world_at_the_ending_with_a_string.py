#search for a word at the ending of a string
import re
str="hello world"
res=re.search(r"world$",str)
if res:
    print("string ends with 'world'")
else:
    print("string does not end with 'world'")