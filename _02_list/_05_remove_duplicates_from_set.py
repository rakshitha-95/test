class Duplicate:
    def remove_duplicate(self,lst):
        self.lst=lst
        temp_lst=[]
        for i in lst:
            if i not in temp_lst:
                temp_lst.append(i)
        lst=temp_lst
        return lst
lst=["rakshitha","varun","vinith","chandana","deekshith","varun"]
obj=Duplicate()
result=obj.remove_duplicate(lst)
print("the final set is ",result)