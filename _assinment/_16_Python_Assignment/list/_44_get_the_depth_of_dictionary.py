'''Get the depth of the dictionary'''
def dict_depth(d):
    if isinstance(d,dict):
        return 1+(max(map(dict_depth,d.values())) if d else 0)
    return 0

dic={'a':1,'b':4,'b':{'c':{'d':{'e':{}}}}}
print(dict_depth(dic))