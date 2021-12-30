'''table of a given number'''
def table(n):
    for i in range(10):
        res=n*i
        print(n,'X',i,'=',res)
    return
n=4
print(table(n))