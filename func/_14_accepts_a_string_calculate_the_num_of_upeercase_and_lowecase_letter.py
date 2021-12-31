'''accepts a string calculate the num of uppercase and number of lowercase letter'''
def calculate_total(str1):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for i in str1:
        if i.isupper():
            d["UPPER_CASE"]+=1
        elif i.islower():
            d["LOWER_CASE"]+=1
        else:
            pass


    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])
str1=("MyNAmeIS RAKSHITHA1234")
calculate_total(str1)