'''sort elments in increasing and decresing order'''
class List:
    def __init__(self,list1):
        self.list1=list1
    def sort_asending(self):
        list.sort(list1)
        return list1
    def sort_decending(self):
        list1.sort(reverse=True)
        return list1

list1=[2,5,5,4,2,2,7,7]
sort_ele=List(list1)
result=sort_ele.sort_asending()
result1=sort_ele.sort_decending()
print("sort elements in assending order:",result)
print("sort elements in decending order:",result1)