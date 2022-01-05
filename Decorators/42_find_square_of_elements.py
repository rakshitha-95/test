#map() function that gives square
def squares(x):
    return x*x
lst=[1,2,3,4,5,6]
lst1=list(map(squares,lst))
print(lst1)