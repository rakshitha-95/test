#same name for global and local variables
a=1
def myfunction():
    a=2
    x=globals()['a']
    print('global var a=',x)
    print('local var a= ',a)
myfunction()
print('global var a=',a)