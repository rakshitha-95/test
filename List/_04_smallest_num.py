'''Smallest number from the list'''
class Smallest:
    def __init__(self,list1):
        self.list1=list1

    def smallest_num(self):
        max = 1
        for i in list1:
            if i<max:
                max=i
        return max

list1=[1,2,3,4,4]
max_num=Smallest(list1)
output=max_num.smallest_num()
print("the maximum number from the list: ",output)