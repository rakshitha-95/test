'''Diffence between  2 list'''
class List1:
    def diference(self,list1,list2):
        self.list1=list1
        self.list2=list2
        return list(set(list1)-set(list2))+list(set(list2)-set(list1))
list1=[7,8,9,6,5,4,5]
list2=[5,6,5,6,3,2]
l=List1()
print(l.diference(list1,list2))

