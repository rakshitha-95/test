''' First,Last elements whose square value is between 1 and 30 except first 5'''
print("First,Last elements whose square value is between 1 and 30 except first 5")
l1=[]
for i in range(3,6):
    value=i*i
    if value>=1 and value<=30:
        l1.append(value)
print(f"first elemebnt is:{l1[0]} and last element is:{l1[-1]}")