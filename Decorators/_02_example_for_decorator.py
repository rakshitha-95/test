'''create a decorator with return value 2'''
def decorator(func):
    def inner():
        x=func()
        x+=1
        print(x)
    return inner()

@decorator
def outer():
    return 40
@decorator
def dec():
    return 33