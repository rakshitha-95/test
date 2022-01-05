'''checking if file exists and then reading data'''
import os,sys
fname=input('enter filename :')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+'does not exists')
    sys.exit()
print('the file contents are :')
str=f.read()
print(str)
f.close()