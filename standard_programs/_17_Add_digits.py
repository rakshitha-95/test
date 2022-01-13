#add digits taken from the user
def addintezer(num,sum=0):
    if 0<=num<10:
        print(num)
    else:
        while num!=0:
            rem=num%10
            sum=sum+rem
            num=int(num/10)
        num=sum

        addintezer(num, sum=0)


num=int(input("enter the num"))
addintezer(num)