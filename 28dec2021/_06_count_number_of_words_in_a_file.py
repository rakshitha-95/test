'''A python programe to count number of lines,words and characters in a txt file'''
import os,sys
fname=input("enter file name :")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+'does not exists')
    sys.exit()
cl=cw=cc=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)
print('N0. of lines: ',cl)
print('no.of words: ',cw)
print('no.of characters: ',cc)
f.close()