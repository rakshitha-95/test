'''find the max of 3 number'''
def maxnum(list1):
    length = len(list1)
    oplist = []
    for i in range(0,length):
        j = i + 1
        while j < length:
            if list1[i] > list1[j]:
                if list1[i] not in oplist:
                    oplist.append(list1[i])
            else:
                if list1[j] not in oplist:
                    oplist.append(list1[j])
            print(oplist)
            j += 1
    return oplist

list1 = []
list1=[int(x) for x in (input("enter the number").split(","))]
oplist = maxnum(list1)
print("Maximum 3 nos: ",oplist)
