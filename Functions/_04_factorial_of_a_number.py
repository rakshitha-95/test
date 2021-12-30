'''Factorial of a number'''
def factorial(n):
    #to find the factorial of n
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(3))




