#python programme totest weather the given num is prime or not
def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
        return x
num=int(input('enter a number:'))
result=prime(num)
if result==1:
    print(num,' is prime ')
else:
    print(num,' is not prime')
