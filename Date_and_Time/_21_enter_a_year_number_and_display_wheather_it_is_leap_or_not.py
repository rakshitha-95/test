#to test wheather leap year or not
from calendar import*
y=int(input('enter year: '))
if(isleap(y)):
    print(y,'is a leap year')
else:
    print(y,'is not leap')