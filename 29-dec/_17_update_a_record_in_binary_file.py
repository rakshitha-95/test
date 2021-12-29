'''A python program to update or modify a record in a binary file'''
#updating the city name in the  file
import os
#take record length as 20 characters
reclen=20
#find size of the file
size=os.path.getsize('cities.bin')
print('size of file={} bytes'.format(size))
#find number of records in the file
n=int(size/reclen)
print('no. of records={}'.format(n))
#open the file in binary mode for reading
with open('cities.bin','r+b') as f:
    name=input('enter the city name:')
    #convert name into binary string
    name=name.encode()

    newname=input('enter new name:')
    #find the length of newname
    ln=len(newname)
    #add spaces to make its length 20
    newname=newname+(ln-20)*' '
    #convert newname into binary string
    newname=newname.encode()
    #position represents the position of file pointer
    position=0
    #found beomes true if city is found in the file
    found=False
    #repeat for n records in the file
    for i in range(n):
        #place te file pointer at position
        f.seek(position)
        #read 20 character
        str=f.read(20)
        #if found
        if name in str:
            print('updated record na:',(i+1))
            found=True
            #go back 20 yeears from current position
            f.seek(-20,1)
            #update the record
            f.write(newname)
        #go to the next record
        position+=reclen
    if not found:
        print('city not found')
