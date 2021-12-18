'''Remove specified index from list and print'''
class List:
    def __init__(self,lst1,index):
        self.lst1=lst1
        self.index=index

    def remove_index(self):
        lst1.pop(index)

        return lst1
lst1=[1,2,5,2,5,8,6]
index=3

l=List(lst1,index)
print(l.remove_index())