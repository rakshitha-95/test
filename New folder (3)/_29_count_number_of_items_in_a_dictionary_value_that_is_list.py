'''count number of items in a dictionary value that is list '''
dict1={'a':[4,8,9,6,5,3],'b':[1,2],'c':[5,4,8,9,7],'d':[4],'e':4}
count=0
for x in dict1:
    if isinstance(dict1[x],list):
        count+=len(dict1[x])
    print(count)