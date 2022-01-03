#variable length argument demo
def add(farg,*args):
    '''to add given num'''
    print('formal argument=',farg)
    sum=0
    for i in args:
        sum+=i
    print('sum of all numbers= ',(farg+sum))
add(5,10)
add(5,10,20,30)
add(2)
