try:
    x=int(input("enter the number"))
    y=int(input("enter the number"))
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("finally")