'''Get the maximum and minimum value in dictionary'''
dict1={'x':896,'y':369,'z':458}
key_max=max(dict1.keys(),key=(lambda k:dict1[k]))
key_min=min(dict1.keys(),key=(lambda k:dict1[k]))
print("Maximum value:",dict1[key_max])
print("Minimum value :",dict1[key_min])