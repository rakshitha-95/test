'''without try-except
print("statement-1")
print(10/0)
print("statement-3")
'''
'''with try-except'''
print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("stmt-3")
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("exception raised and its description is:",msg)
