#finding the day of the year
from datetime import*
#get today's date
td=date.today()
print(td) #display contents of td
#%j returns day of the year as:001,002,...366.
s1=td.strftime("%j")
print('todAY IS',s1,'TH DAY OF THE CURRENT YEAR')
#find the week day name
s2=td.strftime("%A")
print('It is ',s2)