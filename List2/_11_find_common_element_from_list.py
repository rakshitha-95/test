'''Find the common element from the List'''
class List1:
    def __init__(self):
        pass

    def common_element(self,list2):
        d=dict()
        for i in list2:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return d

list2=[1,2,3,4,1,2,3,4,6,6,7,7,7,7]
l=List1()
print(l.common_element(list2))