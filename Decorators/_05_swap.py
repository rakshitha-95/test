var1 = int(input('Enter the first variable:'))

var2 = int(input('Enter the second variable:'))

var1 = var1 ^ var2

var2 = var1 ^ var2

var1 = var1 ^ var2

print ('The value of the first variable after swapping is:', var1)

print ('The value of the second variable after swapping is:', var2)


#using temporary variable we are swapping
vr1 = int(input('Enter the first variable'))

var2 = int(input('Enter the second variable'))

temp = var1

var1 = var2

var2 = temp

print ('The value of the first variable after swapping is:', var1)

print ('The value of the second variable after swapping is:', var2)


#without using temporary variable
var1 = int(input('Enter the first variable'))

var2 = int(input('Enter the second variable'))

var1,var2=var2,var1
print ('The value of the first variable after swapping is:', var1)

print ('The value of the second variable after swapping is:', var2)