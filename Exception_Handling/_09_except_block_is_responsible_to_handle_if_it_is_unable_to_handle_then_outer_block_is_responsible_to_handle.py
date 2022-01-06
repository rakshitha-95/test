try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")