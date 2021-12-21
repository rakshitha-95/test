#reading character from the file
#open file for reading data
f=open('myfile.txt','r')
#read all character from the file
str=f.read()
print(str)
#closing the file
f.close()