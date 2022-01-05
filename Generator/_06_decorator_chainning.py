def decor(func):
    def inner(x):
        value=func(x)
        print("dec1",value)
        if value%2==0:
            # a=value+1
            pass
        return value
    return inner

def decor1(func):
    def inner(x):
        value=func(x)
        print(value)
        if value%2==1:
            print("Not completed")
            pass
        else:
            print("value")
    return inner


@decor1
@decor
def num(x):
    # res=x+1
    # print("hello")
    return x


print(num(4))