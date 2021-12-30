#create phonebook.dat file
#open the file in wb mode as binary file
with open ("phonebook.dat","wb") as f:
    #write data into the file
    n=int(input('how many entries? '))
    for i in range(n):
        name=input('enter name: ')
        phone=input('enter phone number')
        #convert name and phone from strings to bytes
        name=name.encode()
        phone=phone.encode()
        #write the data into the file
        f.write(name+ phone)