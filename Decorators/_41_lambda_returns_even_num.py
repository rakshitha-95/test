'''lambda function that returns even numbers from a list'''
lst=[10,23,45,46,70,99]
lst1=list(filter(lambda x: (x%2==0),lst))
print(lst1)