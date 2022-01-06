#converting the epoch time into date and time
import time
#localtime() converts the epoch time into time_struct object t
t=time.localtime(1641464618.4216633)
#retrieve the data from the structure t
d=t.tm_mday
m=t.tm_mon
y=t.tm_year
print('current date is:%d-%d-%d'%(d,m,y))
#retrieve the time from the structure t
h=t.tm_hour
m=t.tm_min
s=t.tm_sec
print('current time is: %d : %d : %d'%(h,m,s) )