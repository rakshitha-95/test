'''Given a sorted array of distinct integers and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.'''

def search_insert(list1,target):
    for i in list1:
        if target>list1[-1]:
            return len(list1)
        if target<list1[0]:
            return 0
        if(target==i):
            return list1.index(target)
        for i in range(len(list1)):
            if list1[i] >= target:
                return i

list1=[10,13,23,48,69,12,5,67]
list1=sorted(list1)
print(list1)
target=15
print(search_insert(list1,target))

