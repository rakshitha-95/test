'''Multiply all the items in the dictionary'''
def mul(dict1):
    mul=1
    for i in dict1.values():
        mul=mul*i
    return mul
dict1={'a':2,'b':3,'c':4}
print("mul :",mul(dict1))