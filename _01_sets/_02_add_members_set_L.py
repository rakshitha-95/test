'''add members of a set'''
class Set:
    def add(self,set1,set2):
        self.set1=set1
        self.set2=set2
        set1.add(115)
        set2.add("rakvarun")
        return set1,set2

set1={"rakshitha","mcs","python"}
set2={2,3,4,5}
s=Set()
add=s.add(set1,set2)
print("added set is",add)