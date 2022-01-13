'''split a string on the last occurence of the delimeter'''
def split_string(str1):
    l=str1.rsplit(' ',1)[1]
    print(l)

str1='canada japan australia uae india'
split_string(str1)