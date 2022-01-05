''' A decorator is a function that accepts a function as a parameter and returns a function'''
def decor(func):
    def inner(name):
        if name=="Rakshitha":
            print("hello rakshitha good morning")
        else:
            func(name)
    return inner
@decor
def wish(nam):
    print("hello ",nam)
wish("Rakshitha")
wish("varun")