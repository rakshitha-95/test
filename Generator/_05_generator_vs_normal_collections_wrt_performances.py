import random
import time
names=['varun','rakshitha','vinith','deekshith']
subjects=['python','java','.net']
def people_list(num_people):
    results=[]
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subjects)
            }
        results.append(person)
    return results
def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(subjects)
            }
        yield person
t1=time.clock()
people=people_list(10000000)
t2=time.clock()
"""t1=time.clock()
people=people_generator(1000000)
t2=time.clock()"""

print('Took{}'.format(t2-t1))



