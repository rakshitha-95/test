'''remove spaces from dictionary keys'''
dict1={'a':12,'b':3,  'c 2':56}
dict1={x.replace(' ',''):v for x,v in dict1.items()}
print(dict1)