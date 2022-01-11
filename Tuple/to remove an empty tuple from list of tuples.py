#to remove an empty tuple(s) from a list of tuples
list1=[(1,2,3),(5,6),('hello','world'),(),(5,7,4,7)]
list2=[[t for t in list1 if t != ()]]
print(list2)

