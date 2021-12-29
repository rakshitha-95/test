# reading city name based on record number,take record length as 20 character
reclen=20
#open the file in binary mode for reading
with open('cities.bin','rb')as f:
    n=int(input('enter record number: '))
    #move file pointer to the end of n-1 th record
    f.seek(reclen*(n-1))
    #get the nth record with 20 chars
    str=f.read(reclen)
    #convert the byte string into ordinary string
    print(str.decode())