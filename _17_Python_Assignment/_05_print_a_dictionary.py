'''Generate and print a dictionary that contains a number(betwen 1 and n) in the  form(x,x*x)'''
n=int(input("enter the input:"))
d={x:x*x for x in range(1,n+1)}
print(d)