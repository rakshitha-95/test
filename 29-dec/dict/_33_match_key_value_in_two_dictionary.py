'''match key values in two dictionaries'''
x={'key1':1,'key2':3,'key3':4}
y={'key1':1,'key2':2}
for(key,value) in set(x.items())& set(y.items()):
    print('%s: %s is present in both x and y'%(key,value))