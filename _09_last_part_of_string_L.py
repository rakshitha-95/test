class Last:
    def lastpart(self,str1):
        self.str1=str1
        for word in str1.split():
            #    print(word)
            if word == word[-1]:
                pass
        return word
str1="my name is rakshitha"
l=Last()
v=l.lastpart(str1)
print("Last part of string:", v)