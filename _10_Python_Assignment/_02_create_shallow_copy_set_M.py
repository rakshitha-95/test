'''create shallow copy sets'''
import copy
class Set:
    try:
         def shallowcopy(self,lst1):
            self.lst1=lst1
            #self.lst2=lst2
            lst2=copy.copy(lst1)
            print("the original elements before shallow copying")
            for i in range(0,len(lst1)):
                print(lst1[i],end=" ")
            print("/r)")
            lst2[2]=7
            print("the original elements after shallow copying")
            for i in range(0,len(lst1)):
                print(lst1[i],end=" ")
    except Exception as e:
        print("some error is there in the block",e)

lst1=[1,2,3,4,5,5]

obj=Set()
obj.shallowcopy(lst1)