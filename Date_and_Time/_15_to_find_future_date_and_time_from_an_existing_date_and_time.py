#finding future date and time
from datetime import*
#store the date and time in datetime object:d1
d1=datetime(2016,4,29,16,45,0)
#define the duration usingbtimedelta object:period1
period1=timedelta(days=10,seconds=10,minutes=20,hours=12)
#add the duration to d1 and display
print('the new date and time is: ',d1+period1)