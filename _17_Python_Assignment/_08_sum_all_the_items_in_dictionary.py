'''sum all the items in the dictionary'''
def sum(dict1):
    sum=0
    for i in dict1.values():
        sum=sum+i

    return sum
dict1={'a':10,'b':20,'c':52}
print("sum :",sum(dict1))