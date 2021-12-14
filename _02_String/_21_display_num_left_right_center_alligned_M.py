'''To display a number in left right center aligned of width 10'''
num=20
print("the original number is :",num)
print("the number left aligned width(10): "+"{:< 10d}".format(num))
print("the number right aligned width(10): "+"{:10d}".format(num))
print("the number center aligned width(10): "+"{:^10d}".format(num))