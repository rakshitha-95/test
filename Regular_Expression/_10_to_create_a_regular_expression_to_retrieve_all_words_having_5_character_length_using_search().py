#search() will give the first matching word only
import re
str='one two three four five six seven 8 9 10'
result=re.search(r'\b\w{5}\b',str)
#to retrieve the word from result object,use group()
print(result.group())