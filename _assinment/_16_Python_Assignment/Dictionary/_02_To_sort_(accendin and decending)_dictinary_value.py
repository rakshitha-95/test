'''To sort acccending and decending dictionary by value'''
dict1={'rakshitha':1,'varun':2,'deekshit':3,'vinith':4}
a=sorted(dict1.items(),key=lambda x:x[1])
print(a)
b=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
print(b)
