'''print the even number from the list'''
def even_num(list1):
    list2=[]
    for i in list1:
        if i%2==0:
            list2.append(i)
    return list2

list1=[1,5,9,2,3,6,5,4,7,8,9]
print(even_num(list1))