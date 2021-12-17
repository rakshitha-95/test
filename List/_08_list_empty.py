'''check list is empty'''
class List1:
    def __init__(self,mylist):
        self.mylist=mylist

    def empty_set(self):
        if len(mylist)==0:
            return True
        

mylist=list(1.2)
emptylist=List1(mylist)
result=emptylist.empty_set()
print("Is the list is empty :",result)



