'''A python program to create a binary file and store a few records'''
#create cities.bin file with cities names,take the record size as 20 bytes
reclen=20
# open the file in wb mode as binary file
with open("cities.bin","wb") as f:
    #write data into the file
    n=int(input('how many entries?'))
    for i in range(n):
        city=input('enter city name: ')
        #find the length of city
        ln=len(city)
        #increase the city name to 20 chars by adding remaining spaces
        city=city+(reclen-ln)* ' '
        #convert city name into byte string
        city=city.encode()
        #write the city name into file
        f.write(city)
