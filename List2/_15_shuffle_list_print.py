'''Shuffle list and print'''
import random
class List:
    def __init__(self,list1):
        self.list1=list1

    def shuffle_list(self):
        for i in range(len(list1)-1,0,-1):
            j=random.randint(0,i+1)
            list1[i],list1[j]=list1[j],list1[i]

        return list1
list1=[55,66,58,23,69,47,15,]
l=List(list1)
print("the original list is: ",list1)
print(l.shuffle_list())
