'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add
up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].'''
def sum(list1,target):
    list2={}
    for i,j in enumerate(list1):
        rem=target-j
        if rem in list2:
            return [list2[rem],i]
        list2[j]=i
    return[]


list1=[12,7,2,11,15]
target=9
print(sum(list1,target))