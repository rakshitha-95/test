'''check multiple keys exists in a dictionary'''
dict1={"mon":2,"tue":9,"wed":5,"thu":9,"fri":7,}
check_keys={"mon","tue"}
if(dict1.keys()>check_keys):
    print("all keys are presnt")
else:
    print("all keys are not present")
check_keys={"wed","thu"}
if(dict1.keys()>check_keys):
    print("all keys are presnt")
else:
    print("all keys are not present")