try:
    x=int(input("enter the number"))
    y=int(input("enter the numbet"))
    print(x/y)
except ZeroDivisionError:
    print("zeroDivisinerror:can't divide with zero")
except:
    print("default exception:plz provide valid input only")