#retrieve date of births from a string
import re
str='rakshitha 04-08-1995,varun 16-05-1991,vinith 22-09-1997'
res =re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(res)