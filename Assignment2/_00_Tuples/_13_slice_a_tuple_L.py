'''Slice a tuple '''

tuple=(1,2,3,4,5,6,7,8,9)
print(tuple)

#used tuple[start:stop] the start index is inclusive and the stop index
slice = tuple[3:5]
print(slice)

#if the start index isn't defined, is taken from the beg inning of the tuple
slice = tuple[:6]
print(slice)

#if the end index isn't defined, is taken until the end of the tuple
slice = tuple[5:]
print(slice)

#if neither is defined, returns the full tuple
slice = tuple[:]
print(slice)

#The indexes can be defined with negative values
slice = tuple[-8:-4]
print(slice)

#create another tuple
tuple = "HELLO WORLD"
print(tuple)

#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
slice = tuple[2:9:2]
print(slice)

#returns a tuple with a jump every 3 items
slice = tuple[::4]
print(slice)

#when step is negative the jump is made back
slice = tuple[9:2:-4]
print(slice)

