#programme to create a regular expression to replace a string with a new string
import re
str='kumbamele will be conducted at ahmedabad in india'
res=re.sub(r'ahmedabad','allahabad',str)
print(res)