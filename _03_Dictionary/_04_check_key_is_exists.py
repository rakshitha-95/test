'''Check if a given key already exists in a dictionary.'''
class Dict:
    def __init__(self,dict1):
        self.dict1=dict1
    def check_key(self,x):
        if x in dict1:
            print("key is present in dictionary")
        else:
            print("key is not present dictionary")

dict1={"rakshitha":100,"srilekha":90,"seetal":95,"varun":99,"rinky":88}
x="ranjitha"
obj=Dict()
result=obj.check_key(x)

