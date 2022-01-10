#to retrieve the timings either amor pm
import re
str='The meeting may be at 8am or 9am or 4pm or 5pm'
res=re.findall(r'\dam|\dpm',str)
print(res)