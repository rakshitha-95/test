'''remove duplicates'''
list2=[1,2,8,9,8,9,8,5,6,4,5,6]
list1=list(dict.fromkeys(list2))
print(list1)