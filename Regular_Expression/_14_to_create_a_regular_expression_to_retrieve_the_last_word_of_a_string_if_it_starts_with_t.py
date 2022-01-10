#to retrieve the last word of a string'if it starts with t
import re
str='one two three one two three'
result=re.findall(r't[\w]*\Z', str)
print(result)