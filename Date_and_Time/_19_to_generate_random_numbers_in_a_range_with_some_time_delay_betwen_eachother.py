#to generate random numbrs between 100 and 200 every 3.5 secs
import time,random
#generate 10 random numbers
for i in range(10):
    #generate in the range 100 to 200
    num=random.randrange(100,200,5)
    print(num)
    #suspend execution for 3.5 seconds
    time.sleep(0.1)