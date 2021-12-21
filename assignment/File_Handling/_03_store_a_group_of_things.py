#creating a file with strings
#open the file for writting
f=open('myfile.txt','w')
print('enter the text(@ the end):')
str=input()
f.write(str + "\n")
f.close()
