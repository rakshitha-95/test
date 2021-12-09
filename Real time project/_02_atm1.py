print("welcome to ATM machine!!!")
traiels=1
userpin=3759

while traiels!=0:
    pin=int(input("enter the four digit pin number : "))
    if pin!=userpin :
        traiels=-1
        print("wrong pin number, you have ", traiels,"traiels left" )
    else:
        userchoice=str(input("d:Deposit or w:Withdraw "))
        if userchoice=="d":
            userdeposit=int(input("enter the amount would you like to deposit"))
            print(userdeposit ," $ Have been deposited into your account")

        if userchoice=="w":
            userwithdraw=int(input("enter the amount would you like to withdraw"))
            print(userwithdraw ," $ Have been withdrawm from  your account")
    userexit=input("would you like to continue? Y/N")
    if userexit=="N":
        print("thank you")
        break
    else:
        continue




