#to create a regular expression to retrieve alll words having 5 character length
import re
str="one two three four five six seven 8 9 10"
result=re.findall(r'\b\w{5}\b',str)
print(result)