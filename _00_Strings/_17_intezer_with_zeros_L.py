'''print the following intezer with zeros on the left of specified width'''
def intezer_num():
    a=123
    print("original number :",a)
    print("formating the num left padding width 3 : "+"{:0>4d}".format(a))
    a = 5
    print("original number :", a)
    print("formating the num left padding width 5 : " + "{:0>2d}".format(a))
intezer_num()

