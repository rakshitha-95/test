#create a regular expression to retrieve all words starting with a in the given string
import re
str=' an apple a day keeps the doctor away'
result=re.findall(r'\ba[\w]*\b',str)
#findall() returns a list, retrieve the eleements from the list
for word in result:
    print(word)