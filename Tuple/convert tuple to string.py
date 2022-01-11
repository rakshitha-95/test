#using for loop
tuple1=('a','b','g','y','h','o')
string1=''
for i in tuple1:
    string1=string1+i
print('the converted string is:',string1)

#using reduce
from functools import reduce
tuple2=('a','b','g','y','h','o')
tuple3=reduce(lambda a,b:a+b,tuple2)
print('the converted tuple using reduce',tuple3)

#using join
tuple1=('a','b','g','y','h','o')
string2=''.join(tuple1)
print('using join',string2)


my_tuple_data = ("This", "is", "a", "sample", 44, 55, 66, "program")
delimiter = ' '
# Convert list of items to a string value
final_str = delimiter.join(map(str,my_tuple_data))
print(final_str)