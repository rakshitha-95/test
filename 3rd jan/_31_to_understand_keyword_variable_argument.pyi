#keyword variable argument demo
def display(farg,**kwargs):
    print('formal argument=',farg)
    for x,y in kwargs.items():
        print('key{},value={}'.format(x,y))
display(5,rollno=10)
display(5,rollno=10,name='rakshitha')
