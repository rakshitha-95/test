'''multiply of elements'''
class List:
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        return (a*b)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
multiply=List()
result=multiply.mul()
print("the multiplication of two numbers is :",result)

