'''count words in string'''
class Count:
    def words_count(self,str1):
        self.str1=str1

        return len(str1.split())


str1="my name is rakshitha"
c=Count()
count=c.words_count(str1)
print("the no of words in string is",count)