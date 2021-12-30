'''A python program to delete a specific record from the binary file'''
#deleting a record from the file
import os
#take record length as 20 character
reclen=20
#find size of the file
size=os.path.getsize('cities.bin')
#find number of records in the file
n=int(size/reclen)
#open the cities.bin for reading
f1=open('cities.bin','rb')
#open file2.bin for writting
f2=open('file2.bin','wb')
#accept city name from keyboard
city=input('enter city name to delete:')
#add spaces so that it will have 20 characters length
ln=len(city)
city=city+(reclen-ln)*' '
#convert city name to binary string
city=city.encode()
#repeat for all the n records
for i in range(n):
    #read one record from f1 file
    str=f1.read(reclen)
    #if it is not the city name,store into f2 file
    if(str!=city):
        f2.write(str)
print('record deleted')
#close the files
f1.close()
f2.close()
#delete the cities.bin file
os.remove("cities.bin")
#rename file2.bin as cities.bin
os.rename("file2.bin","cities.bin")