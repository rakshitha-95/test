'''compute the similarity between two lists'''
list1=[45,23,69,56,85,96]
list2=[45,89,69,58,63,52]
print(list1)
print(list2)
res=len(set(list1) and set(list2))/ float(len(set(list1)| set(list2)))*100
print("percentage among the list is",res)