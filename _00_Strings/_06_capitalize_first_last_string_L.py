'''''capitalize first and last character of a string'''
class Capitalize:
    def capital1(self,str1):
        self.str1=str1
        word=" "
        for str1 in str1.split(" "):
            word+=str1[0:1].capitalize()+str1[1:-1]+str1[-1].upper()+" "

        return word

str1="my name is rakshitha"
c=Capitalize()
string1=c.capital1(str1)
print("the capitalize first and last character of a string ",string1)



