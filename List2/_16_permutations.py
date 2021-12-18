'''All permutations of element'''
import itertools
class List:
    def __init__(self,list1):
        self.list1=list1

    def permutations(self):
        res=list(itertools.product(*list1))
        print(res)


list1=[1,9,6,5,8,7,5]
l=List(list1)
print(l.permutations())