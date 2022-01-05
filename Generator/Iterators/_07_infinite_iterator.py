#infinite iterators
class Infinite:
    def _iter_(self):
        self.num=1
        return self
    def _next_(self):
        num=self.num
        self.num+=5
        return num
obj=Infinite()
myiter=iter(obj)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Its going to infinte...if we want to stop that
#stopiterate method
#anything that can be loop over in python ---iterable
#To check the list has iter...
'''num=[1,2,3,4]
print(dir(num))
'''