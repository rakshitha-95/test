'''A pyhton programe to search for city name in the file and display the record number that contains the city name'''
#searching teh city name in the file
import os
#take record length as 20 character
reclen=20
#find the size of the file
size=os.path.getsize('cities.bin')
print('size of the file={}bytes'.format(size))
#find the number of records in the file
n=int(size/reclen)
print('no.of records ={}'.format(n))
#open the file in binary mode for reading
with open('cities.bin','rb') as f:
    name=input('enter the city name :')
    #convert name into binary string
    name=name.encode()
    #position represents the position of file pointer
    position=0
    #found becomes True if city is found in the file
    found=False
#repeat for n records in the file
    for i in range(n):
    #place the file pointer at position
        
        f.seek(position)
        #read 20 characters
        str=f.read(20)
        #if found
        if name in str:
            print('found at record no: ',(i+1))
            found=True
        #go to next record
        position+=reclen
    if not found:
        print('city not found')

