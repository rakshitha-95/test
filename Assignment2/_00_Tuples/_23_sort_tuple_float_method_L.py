'''Sort a tuple by its float method'''
def sort(tup):
    return(sorted(tup,key=lambda x: float(x[1]),reverse=True))

tup =[('rak','12.44'),('var','14.5'),("vin",'16.5'),('deek','17.5')]
print(sort(tup))