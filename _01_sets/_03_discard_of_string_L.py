'''Discard of a String'''
class Set:
    def discard1(self,set1):
        self.set1=set1
        res=set1.discard('yellow')
        return res


set1={'black','green','white','yellow'}
s=Set()
output=s.discard1(set1)
print(output)
print(set1)