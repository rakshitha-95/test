#to know who is older
from datetime import *
#enter birth dates and store into date class objects
d1,m1,y1=[int(x) for x in input("enter first person's birth date(MM/YYYY): ").split('/')]
b1=date(y1,m1,d1)
d2,m2,y2=[int(x) for x in input("enter first person's birth date(MM/YYYY): ").split('/')]
b2=date(y2,m2,d2)

#compare the birth dates b1==b2:
if b1==b2:
    print('both persons are of equal age')
elif b1>b2:
    print('the second person is older')
else:
    print('the first person is older')
