try:
    x=int(input("enter the number"))
    y=int(input("enter the number"))
    print(x/y)
except ArithmeticError:
    print("arithmetic Error")
except ZeroDivisionError:
    print("zerodivision Error")