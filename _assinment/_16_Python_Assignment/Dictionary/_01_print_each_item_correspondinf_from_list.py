'''print each item and its corresponding type from the following list'''
datalist=[1452,11.23,1+2j,True,'Rakshitha',(0,-1),[15,12],{"class":'V',"section":'A'}]
for item in datalist:
    print("Type of",item,"is",type(item))