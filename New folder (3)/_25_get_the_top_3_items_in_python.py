'''get the top three items in python'''
from heapq import nlargest
from operator import itemgetter
items={'item1':85,'item2':55,'item3':15,'item4':15,'item5':75,'item6':965,}
for name,value in nlargest(3,items.items(),key=itemgetter(1)):
    print(name,value)