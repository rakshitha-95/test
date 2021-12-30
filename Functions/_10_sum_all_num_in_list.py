'''sum all num in list'''
def sum_num(list1):
    for i in range(0,len(list1)):
        res=sum(list1)
        return res
list1=[1,2,3,4]
print(sum_num(list1))
