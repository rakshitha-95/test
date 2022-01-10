#reads emails ids from a text file
import re
#open the file for reading
f=open('mail.txt','r')

#repeat for each line of the file
for line in f:
    res =re.findall(r'\S+@\S+',line)
#display if there are some elements in result
if len(res)>0:
    print(res)
#close the file
f.close()