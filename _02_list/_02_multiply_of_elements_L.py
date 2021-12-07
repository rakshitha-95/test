class Multiply:
    def multiply1(self,lst):
        self.lst=lst
        result=1
        for x in lst:
            result=result*x

        return result

lst=[4,5,6,7,8,9]
obj=Multiply()
product=obj.multiply1(lst)
print("the multiplication of the elements",product )