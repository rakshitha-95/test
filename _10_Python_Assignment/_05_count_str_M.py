class Prgm:
    def count_str(self,string,word1):
        self.string=string
        self.word1=word1
        try:
            for ele in string.split():
                if ele == word1:
                    pass
            print(string.count(word1))
        except Exception as e:
            print('the error is ',e)
string = str(input("Enter your string:"))
word1 = str(input("Enter your word:"))
obj=Prgm()
obj.count_str(string,word1)