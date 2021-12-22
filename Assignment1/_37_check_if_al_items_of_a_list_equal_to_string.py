'''check if all items of a list is equal to given string'''
list1=["green","red","black","white","orange"]
list2=["green","green","green","green"]
print(all(c=='blue' for c in list1))
print(all(c=='green' for c in list2))