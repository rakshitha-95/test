class Set:

    def frozen_set(self,t1):
        try:
            self.t1=t1
            fnum=frozenset(t1)
            print("the frozen set is",fnum)
        except Exception as e:
            print("there is some error",e)
t1=(1,2,3,4,5,5,6)
obj=Set()
obj.frozen_set(t1)