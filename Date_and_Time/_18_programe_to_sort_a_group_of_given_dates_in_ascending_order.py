#sorting dates
from datetime import*
#take an empty list
group=[]
#add today's date to list,i.e.2016-04-30
group.append(date.today())
#create some more dates snd add them to list
d=date(2015,6,29)
group.append(d)
d=date(2014,6,30)
group.append(d)
#add 25 days to the date and add to list
group.append(d+timedelta(days=25))
#sort the list
group.sort()
#display sorted dates
for d in group:
    print(d)