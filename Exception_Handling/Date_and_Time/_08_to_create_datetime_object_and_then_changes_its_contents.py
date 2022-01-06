#creating datetime object and change its contents
from datetime import*
#create a datetime object
dt1=datetime(year=2016,month=6,day=24,hour=15,minute=30,second=15)
print(dt1)
#change its year,month and hour values
dt2=dt1.replace(year=2022,hour=5,month=1)
print(dt2)