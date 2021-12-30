'''convert list,tuple,set to list,tuple,set'''
#list to tuple
def convert(list1):
    return(*list1,)
list1=[1,5,9,8,7,6,6]
print(convert(list1))
#list to set
def convert(list1):
    return set(list1)
print(convert(list1))
#tuple t0 list
def convert(tup1):
    result=[]
    for i in tup1:

            result.append(i)
    return result
tup1=(7,9,6,8,5,3,2,4,5)
print(convert(tup1))
#tuple to set
def convert(tup1):
    return set(tup1)
print(convert(tup1))
#set to list
set1={1,2,3,8,12,85}
def convert(set1):
    return list(set1)
print(convert(set1))
#set to tuple
def convert(set1):
    return (*set1,)
print(convert(set1))




