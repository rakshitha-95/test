'''take a list and returns a new list with unique elments '''
def unique_elements(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)

    return list2
list1=[1,5,9,9,6,3,2,5,8,7,5,3,1,5,9]
print(unique_elements(list1))
