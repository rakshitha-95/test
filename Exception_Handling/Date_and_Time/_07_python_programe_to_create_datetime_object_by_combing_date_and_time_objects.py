'''A python programme to create datetime object by combing date and time objects'''
#combing date and time
from datetime import*
d=date(2022,1,6)
t=time(5,10)
dt=datetime.combine(d,t)
print(dt)