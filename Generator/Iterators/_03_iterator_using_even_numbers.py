#creating an iterator that generates sequence of even numbers:
class Even:
    def _init_(self,max):
        self.n=2
        self.max=max
    def _iter_(self):
        return self
    def _next_(self):
        if self.n <= self.max:
            result=self.n
            self.n+=2
            return result
        else:
            raise StopIteration

numbers=Even(10)
print(next(numbers))