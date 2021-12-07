class Sum:
    def listsum(self,lst):
        self.lst=lst
        total = 0
        i = 0
        while i < len(lst):
            total = total + lst[i]
            i = i + 1
        return total

lst=[1,2,3,4]
s=Sum()
sum1=s.listsum(lst)
print("sum of the set is",sum1)



