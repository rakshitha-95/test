'''largest number from the list'''
class Largest:
    def __init__(self,list1):
        self.list1=list1

    def largest_num(self):
        max = 0
        for i in list1:
            if i>max:
                max=i
        return max

list1=[1,2,3,4,4]
max_num=Largest(list1)
output=max_num.largest_num()
print("the maximum number from the list: ",output)