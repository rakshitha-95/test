class Smallest:
    def smallestnum(self,lst):
        self.lst=lst
        max=lst[0]
        for x in lst:
            if x< max:
                max=x

        return max
lst=[4,5,7,9,70,55,77,88]
obj=Smallest()
min_value=obj.smallestnum(lst)
print("the minimum value of the lst is ",min_value)
