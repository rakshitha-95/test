'''print the following intezer with * on the right of specified width'''
def intezer_num():
    a=1
    print("original number :",a)
    print("formating the num right padding width 2 :"+"{:*<2d}".format(a))
    a = 14585
    print("original number :", a)
    print("formating the num right padding width 2 :" + "{:*<6d}".format(a))
intezer_num()