'''Generate all sublist'''
from itertools import combinations
def sublist(list1):
    list2=[]
    for i in range(0,len(list1)+1):
        temp=[list(x) for x in combinations(list1,i)]
        if len(temp)>0:
            list2.extend(temp)
    return list2

list1=[10,20,30,40]
list2=['x','y','z']
print("original list :",list1)
print(sublist(list1))