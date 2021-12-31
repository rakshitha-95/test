'''check weather a given number is in range'''
def num(list1,n):
    if n in range(0,12):
        print("the num is in range")
    else:
        print("the num not in range")


list1=[1,5,6,8,9,12]
n=2
num(list1,n)