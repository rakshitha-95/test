'''convert a string in a list'''
def convert(str1):
    li=list(str1.split(" "))
    return li

str1="i am going to office now!!"
print(convert(str1))