numbers=(1,2,3,4,5)
print(numbers)

#accept a new element and position number

list1=[int(input('enter new element:'))]
new=tuple(list1)
position=int(input('Enter position number:'))
num1=numbers[0:position-1]
num1=num1+new
numbers=num1+numbers[position:]
print(numbers)