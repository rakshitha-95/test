'''A python programe using filter() to filter outbeven numbers from a list'''
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
lst=[10,23,45,46,77,99]
lst1=list(filter(is_even,lst))
print(lst1)
