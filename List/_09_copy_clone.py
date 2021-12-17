'''copy or clone'''
class List:
    def __init__(self,cl):
        self.cl=cl

    def copyandcloning(self):
        copylist=cl
        print(copylist)
        clone1=copylist
        print(clone1)
        return

cl=[45,25,63,89,56,48]
clone=List(cl)
result=clone.copyandcloning()
print("copy or clone :",result)