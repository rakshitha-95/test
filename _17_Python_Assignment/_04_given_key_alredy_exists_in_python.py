'''Check if a given key is alredy exists in python'''
def checkkey(dict,key):
    if key in dict.keys():
        print("present, ", end=" ")
        print("value=",dict[key])
    else:
        print("not present")

dict={'a':100,'b':200,'c':300,'d':400}
key='b'
checkkey(dict,key)