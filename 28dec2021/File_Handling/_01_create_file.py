#creating a file to store characters
#open the file for writting data
f=open('myfile.txt','a')
#enter character from keyboard
str=input("enter text: ")
#writing the atring into file
f.write(str)
f.close()