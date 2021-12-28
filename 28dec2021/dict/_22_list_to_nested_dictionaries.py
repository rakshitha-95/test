'''convert a list into a nested dictionaries of keys'''
list=[1,2,3,4,5,6]
dict1=current=  {}
for i in list:
    current[i]={}
    current=current[i]
print(dict1)