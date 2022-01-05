class Powtwo:
    def __init__(self,n,max=0):
        self.max=max
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n>=self.max:
            result=2**self.n
            self.n-=1
            return result
        else:
            print("stopping iteration")

'''
print("-------PowTwo For loop----------")
for i in myobj():
    print(i)
'''

print("-----PowTwo Manual iteration--------------")
#Now we can create an iterator and iterate through it as follows.
myObj = Powtwo(7)
print(myObj)

myIter = iter(myObj) # myObj.__iter__()
'''
print(next(myIter))  # or myIter.__next()__
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
# print(next(myIter)) # 9th time
'''

print("------Auto for loop------")
print(type(myIter))
print(type(myObj))

print(myObj.__next__())
print(myObj.__next__())

for i in range(7):
    print(myObj.__next__())












