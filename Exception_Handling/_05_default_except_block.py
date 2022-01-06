try:
    print(10/0)
except:
    print("Default Except")
except ZeroDivisionError:
print("ZeroDivisionError") 