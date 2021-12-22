'''Split a list every nth element'''
c=['a','b','c','d','e','f','g','h','i','j','l']
def list_slice(c,step):
    return[c[i::step] for i in range(step)]
print(list_slice(c,3))

list_slice(c,3)