'''merge two dictionary'''
class Dict:
    def merge_dict(self,dict1):
        self.dict1=dict1

        dict1.update({"ranjitha":50})
        print(dict1)
dict1={"rakshitha":100,"srilekha":90,"seetal":95,"varun":99,"rinky":88}


obj=Dict()
obj.merge_dict(dict1)