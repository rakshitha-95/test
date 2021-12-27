'''Merge two python dictionaries'''
def merge(dict1,dict2):
    return(dict2.update(dict1))

dict1={'a':10,'b':20,'c':52}
dict2={'d':96,'e':69,'f':78}
print(merge(dict1,dict2))
print(dict2)
