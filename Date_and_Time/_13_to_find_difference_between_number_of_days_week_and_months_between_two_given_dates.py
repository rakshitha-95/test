#difference days,weeks and months between two dates
from datetime import *
#enter two dates from the keyboard
d1,m1,y1=[int(x) for x in input("enter first date: ").split('/')]
d2,m2,y2=[int(x) for x in input("enter second date: ").split('/')]

#create date class objects with the input
dt1=date(y1,m1,d1)
dt2=date(y2,m2,d2)
#find days difference between these two dates
dt=dt1-dt2
print('Days difference= ',dt)

#find difference in weeks
weeks,days=divmod(dt.days,7)
print('weeks difference= ',weeks)

#find difference in months
months,days=divmod(dt.days,30)
print('months difference=',months)
