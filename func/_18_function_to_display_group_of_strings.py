'''function to display group of strings'''
from itertools import groupby
def group_string(str1):
    ele='is'
    res = [list(j) for i, j in groupby(str1, lambda x: x == ele) if not i]
    return res
str1="my, name, is, rakshitha"
print(group_string(str1))