'''map two lists into a dictionary'''
keys=['name','age','job']
values=['Rakshitha',27,'Developer']
dict1={k:v for k,v in zip(keys,values)}
print("Dictionary Items :",dict1 )
