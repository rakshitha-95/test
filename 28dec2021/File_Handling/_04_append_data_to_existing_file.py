#appending and then reading strings
#open the file for reading data
f=open('myfile.txt','a+')
print('enter text to append data')
str=input()
f.write(str+"\n")
print(str)
f.close()