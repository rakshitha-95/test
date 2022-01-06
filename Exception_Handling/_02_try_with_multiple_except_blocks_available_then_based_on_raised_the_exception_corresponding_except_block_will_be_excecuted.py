try:
    x=int(input("enter the input"))
    y=int(input("enter the input"))
    print(x/y)
except ZeroDivisionError:
    print("cant divide with zero")
except ValueError:
    print("please provide int value only ")

