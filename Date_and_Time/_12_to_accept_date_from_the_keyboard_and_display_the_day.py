#finding day of the week
from datetime import *
#accept date,month and year from the keyboard
d,m,y=[int(x) for x in input("enter a date: ").split('/')]
#store them in date class object 'dt'
dt=date(y,m,d)
#%w-day number and %A full name of the week day
print(dt.strftime('day %w of the week. This is %A'))