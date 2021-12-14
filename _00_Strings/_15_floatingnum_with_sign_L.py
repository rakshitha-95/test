''' print the floating number upto 2 decimal points with sign'''
def floating_num():
    float=-56.45588
    format_float="formatted number "+" {:.2f}".format(float)
    print(format_float)

floating_num()