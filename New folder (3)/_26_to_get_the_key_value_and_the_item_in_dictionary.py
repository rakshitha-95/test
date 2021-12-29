'''to get the key,value and item in dictionary'''
dict1={1:10,2:45,3:56,4:67,6:89,7:90,8:89}
for count,(key,value) in enumerate(dict1.items(),1):
    print(key,' ',value,' ',count)
