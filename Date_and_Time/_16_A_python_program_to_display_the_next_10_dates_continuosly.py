
#displaying a range of continuoous dates
from datetime import*
#start with today
d=date.today()
print(d)
#or any other date
#d=date(1996,6,29)
#add 1 to 9 days and get future dates
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)