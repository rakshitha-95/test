'''unzip a list of tuples into indiviual lists'''

tuple=[(2,3),(4,5),(6,7)]
print(tuple)
print(list(zip(*tuple)))


#unzip into lists
tuple= [(1, 2), (3, 4), (8, 9)]
print([list(t) for t in zip( * tuple)])
