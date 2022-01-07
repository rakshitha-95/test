#diffences between two dates  a long with times
from datetime import*
#create two datetime objects that store date and time
d1=datetime(2000,6,25,8,00,25)
d2=datetime(2016,5,20,7,55,15)

#find the difference in days and time
diff=d2-d1
print(diff)
#divide days by 7 to get weeks and remainning days
weeks,days=divmod(diff.days,7)
#divide seconds by 3600 to get hours and remainning seconds
hrs,secs=divmod(diff.seconds,3600)
#divide remainning seconds by 60 to get minutes
mins=secs//60
#take temainning seconds from the remainder of division
secs= secs%60
print('difference is %d weeks,%d days,%d hours,%d minutes and %d seconds'% (weeks,days,hrs,mins,secs))