'''Get unique values'''
def unique(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print (x)


list1=[12,23,23,36,36,36,26,56]
print("\nthe unique values are :")
unique(list1)