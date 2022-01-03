'''Acessing the global variable inside a function'''
a=1
def myfunction():
    global a
    print('global a=',a)
    a=2
    print('modified a=',a)
myfunction()
print('global a=',a)