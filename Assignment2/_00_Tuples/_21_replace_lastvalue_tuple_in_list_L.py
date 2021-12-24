'''replace a last value of tuples in a list'''

tuple=[(10,20,30),(40,50,60),(60,70,80)]
print([t[:-1] + (100,) for t in tuple])