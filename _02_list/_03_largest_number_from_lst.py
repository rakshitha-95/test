class Largest:
    def largestnum(self,lst):
        self.lst=lst
        max=lst[0]
        for x in lst:
            if x> max:
                max=x

        return max
lst=[4,5,7,9,70,55,77,88]
obj=Largest()
max_value=obj.largestnum(lst)
print("the maximum value of the lst is ",max_value)
