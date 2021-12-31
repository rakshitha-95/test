'''to match the item in two dictionaries'''
def item(x,y):
    for (key, value) in set(x.items()) & set(y.items()):
        print('%s: %s is present in both x and y' % (key, value))

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
item(x,y)
