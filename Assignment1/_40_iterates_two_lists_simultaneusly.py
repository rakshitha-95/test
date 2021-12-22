'''iterates over two lists simultaneously'''
list1=['rakshitha','varun','vinith','deekshith','ranjitha']
list2=['a','b','c','d','e']
for (a,b) in zip(list2,list1):
    print(a,b)