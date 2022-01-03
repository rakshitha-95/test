#same name for global and local variables
a=1
def myfunction():
    a=2
    print('a = ',a)
myfunction()
print('a = ',a)
    