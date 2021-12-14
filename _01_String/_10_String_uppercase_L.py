'''Convert  a given String to all upprcase'''

class String:
    def is_upper(self,str1,str2):
        self.str1=str1
        self.str2=str2
        print(str1.upper())
        print(str2.lower())


str1="my name is rakshitha"
str2="I AM FROM RAJAGINAGAR"
obj=String()
obj.is_upper(str1,str2)


