'''convert a list of tuple into dictionary'''
list=[("Rakshitha",90),("varun",95),("vinith",85)]
dict1=dict()
for students,score in list:
    dict1.setdefault(students,[]).append(score)
    print(dict1)

def convert(list,dict1):
    dict1=dict(list)
    return dict1

list=[("Rakshitha",90),("varun",95),("vinith",85)]
dictionary={}
print(convert(list,dictionary))