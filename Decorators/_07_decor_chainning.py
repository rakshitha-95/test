def decor(func):
    def inner(name):
        print("First Decor(decor)Function Execution")
        func(name)
    return inner
def decor1(func):
    def inner(name):
        print("Second Decor(decor1)Execution")
        func(name)
    return inner
@decor
@decor1
def wish(name):
    print("hello",name,"Good Morning")

wish("rakshitha")