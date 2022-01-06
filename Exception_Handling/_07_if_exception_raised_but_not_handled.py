'''if there is an exception raised but not handled'''
try:
    print("try")
    print(10/0)
except NameError:
    print("NameError")
finally:
    print("finally")