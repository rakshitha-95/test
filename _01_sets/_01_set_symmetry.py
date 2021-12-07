'''create set symmetry'''

class Symmetry:
    def setsymmetry(self,set1,set2):
        self.set1=set1
        self.set2=set2
        return (set1.symmetric_difference(set2))
set1={1,2,3,4,5}
set2={4,5,6,7}
s=Symmetry()
set=s.setsymmetry(set1,set2)
print("the output of the set symmetry" ,set )

