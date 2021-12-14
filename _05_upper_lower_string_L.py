'''upper lower of the string'''

class Upper:
    def isupper(self,str1):
        self.str1=str1
        for i in str1:
            return str1.upper()

str1="my name is rakshitha"
u=Upper()
uppercase=u.isupper(str1)
print("the upper of the string is ",uppercase)