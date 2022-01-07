#formatting the current time
from datetime import*

#create datetime object with current date and tme
dt=datetime.now()
print(dt)
#display only time
print('current time: ', dt.strftime("%H:%M:%%S"))