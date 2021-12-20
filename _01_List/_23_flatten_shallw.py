'''Flatten a shallow'''
def flatten(list1):
    return[x for y in list1 for x in y]

list1=[[1,2,3],[4,8,5,8,6,5]]
print("the original list is: ",list1)
print("the flatten list is: ",flatten(list1))