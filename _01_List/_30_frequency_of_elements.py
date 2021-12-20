'''Frequency of elements'''
d={}
list1=[[1,2,3],[4,5,6],[7,8,9]]
for x in list1:
    for i in x:
        d[i]=d.get(i,0)+1

# Orignal list
print(f"The original list : {list1}")

# printing result
print(f"The list frequency of elements is : {d}")