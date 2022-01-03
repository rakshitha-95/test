'''function to accept a group og numbers and find their total average'''
#a function to find total and average
def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum+=i
        avg=sum/n
    return sum,avg
print('enter numbers seperated by space: ')
lst=[int(x) for x in input().split()]
#call calculate() and pass the list
x,y=calculate(lst)
print('total: ',x)
print('average: ',y)