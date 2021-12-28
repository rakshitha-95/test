'''Remove duplicate value from dictionary'''
dict1={'a':45,'b':89,'c':96,'d':23,'e':23}
temp=[]
res=dict()
for key,val in dict1.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print("the dict after removing the dupicates :",res)