'''Reverse a string'''
def reverse(str1):
    str=""
    for i in str1:
        str=i+str
    return str
str1="i have to finish the task"
print("original string is :",end="")
print(str1)
print("the reversed string is:",end="")
print(reverse(str1))