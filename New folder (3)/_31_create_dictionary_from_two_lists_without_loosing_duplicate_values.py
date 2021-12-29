'''crete a dictionary from two lists without loosing duplicate values'''
from collections import defaultdict
class_list=['class5','class6','class7','class8']
id_list=[1,2,2,3]
temp=defaultdict(set)
for c,i in zip(class_list,id_list):
    temp[c].add(i)
print(temp)
