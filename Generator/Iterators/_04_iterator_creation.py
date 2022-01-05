#To create an iterator, we need to implement the methods
#iter() and next().
class Example:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        x=self.a
        self.a+=2
        return x
iterator=Example()
my_iter=iter(iterator)
print(next(my_iter))
print(next(my_iter))