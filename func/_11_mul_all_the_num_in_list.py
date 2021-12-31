'''multiply all the elements in the list'''
def multify_num(list1):
    mul = 1
    for i in list1:
        mul=mul*i
    return mul

list1=[1,2,3,4]
print(multify_num(list1))