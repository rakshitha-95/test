'''add key to the dictionay'''
class Dict:
    def add_key(self,dict1):
        self.dict1=dict1
        dict1['rakshitha']=44
        return dict1
dict1={"varun":31,"ranjitha":17,"sharath":15}
obj=Dict()
result=obj.add_key(dict1)
print("the final dict is",result)


