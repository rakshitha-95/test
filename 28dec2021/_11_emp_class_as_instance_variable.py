'''A python programme to pickle an Emp class with employee details as instance variables'''
import Emp,pickle

f=open('emp.dat','wb')
n=int(input('how many employees?'))
for i in range(n):
    id=int(input('enter id:'))
    name=input('enter name: ')
    sal=float(input('enter salary:'))

    e=Emp.Emp(id,name,sal)
    pickle.dump(e,f)
f.close()
