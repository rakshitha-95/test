f=open('myfile1.txt','w')
for i in range(13):
    str=input('enter text:')
    f.write(str+'\n')
f.close()


#we have created a textfile file and wrote some text
f=open('myfile1.txt','r')
for iline in range(13):
    str=f.readline()
    if iline==9:
        print('tenth line',str)

f.close()
