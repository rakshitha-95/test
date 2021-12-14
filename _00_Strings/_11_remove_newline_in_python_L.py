'''Python programe to remove new line'''
class String:
    def remove_line(self,str1):
        self.str1=str1
        print(str1)
        print(str1.rstrip())

str1="my name is rakshitha\n"
obj=String()
obj.remove_line(str1)