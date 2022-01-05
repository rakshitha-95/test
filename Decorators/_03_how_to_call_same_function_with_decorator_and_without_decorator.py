'''we should not use @decor'''
def decor(func):
    def inner(name):
        if name=="Rakshitha":
            print("hello rakshitha good morning")
        else:
            func(name)
    return inner
def wish(name):
    print("hello ",name,"morning")
decorfunction=decor(wish)
decorfunction("raks")
decorfunction("var")
decorfunction("Rakshitha")