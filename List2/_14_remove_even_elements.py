"Remove even elements and print list"
class List:
    def __init__(self,list1):
        self.list1=list1

    def remove_even(self):
        list2=[]
        for i in list1:
            if i %2 !=0:
                list2.append(i)
        return list2


list1=[2,8,6,4,3,6,69,33,55,77]
l=List(list1)
print(l.remove_even())