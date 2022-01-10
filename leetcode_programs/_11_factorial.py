''''#using recursion
def factorial(num):
    if (num==1) or (num==0):
        return 1
    else:
        return num*factorial(num-1)

num=0
result=factorial(num)
print(result)
'''
#using for loops
number=4
result1=1
for i in range(1,number+1):
    result1=result1*i
print(result1)