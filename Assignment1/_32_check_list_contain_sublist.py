'''checck a list contain a sublist'''
list1=[2,3,5,6,7,8]
sublist=[2,3,5]
res=False
for index in range(len(list1)-len(sublist) +1):
    if list1[index:index +len(sublist)]==sublist:
        res=True
        break

print("Is sublist present in list ?:" ,res)