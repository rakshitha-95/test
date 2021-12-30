'''fibonaccy series'''
# def Fibonacci(n):
#     if n<0:
#         print("incorrect input")
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
#
# n=9
# print(Fibonacci(n))




def  feb(n):
    first=0
    print(first)
    second=1
    print(second)
    for i in range(n-1):
        third=first+second
        print(third)
        first=second
        second=third

feb(9)