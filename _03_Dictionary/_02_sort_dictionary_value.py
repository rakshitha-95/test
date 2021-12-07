'''sort the dictionary'''
class Dict:
    def dict_sort(self,dict1):
        self.dict1=dict1
        return dict(sorted(dict1.items(),key=lambda x: x[1]))
        #return dict(sorted(dict1.items()))


dict1={"rakshitha":100,"srilekha":100,"seetal":95,"varun":99,"rinky":88}
obj=Dict()
result=obj.dict_sort(dict1)
print("the sorted dict is",result)