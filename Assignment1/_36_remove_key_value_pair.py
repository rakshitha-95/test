'''Remove a key value pairs from a list of dictionaries'''
list1=[{'a':1,'b':2},{'a':3,'b':4}]
print(list1)
list2=[{k:v for k,v in d.items() if k!='b' } for d in list1]
print(list2)
