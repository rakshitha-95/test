'''counting number elements within a specified ranges'''
def count_inc_range_list(list1,min,max):
    count=0
    for i in list1:
        if min <= i <=max:
            count+=1
    return count

list1=[1,2,3,4,5,8,9,10,10,11,16,18,19,5,2,1,2]
print(count_inc_range_list(list1,3,20))


