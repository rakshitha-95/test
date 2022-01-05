print('---------Iterator For loop Mechanism-----------')
my_list = [4, 7, 0, 3]
print(my_list)  #  my_list.__str__()
for each in my_list:
    print(each)

my_list = [4, 7, 0, 3]        # 1. Define a list
my_iter = my_list.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print("---------Iterator Internal Mechanism-----------")

try:
    print(my_iter.__next__())  # 3. Iterate through it using __next()__
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__()) # This will raise exception, as no items left in my_list
except StopIteration as si:
    print("Stopping iterations")

list1=["rakshiths","varun","deekshith"]
my_list1=iter(list1)
print(my_list1)
print(next(my_list1))
