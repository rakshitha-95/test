'''Find the count of charater by using the build in function'''

"Find the count of the charater by using the build in function:"
str = input("Enter the string:")
res=str.count("e")
print(res)

"Find the count of charater by using for loop"

word = "are"
for i in str.split():
    if i == word:
        print(str.count(word))

"Find the count of charater by using functions:"

def count_str(string,word1):
    for ele in string.split():
        if ele == word1:
            pass
    print(string.count(word1))
string = input("Enter your string:")
word1 = input("Enter your charater:")
count_str(string,word1)


"Find the count of charater by using oops:"

class Strcount:
    def str1_count(self,str1,word):
        self.str1=str1
        self.word=word
        for i in str1.split():
            if i==word:
                pass

        return str1.count(word)
str1="iam good"
word="good"
s=Strcount()
a=s.str1_count(str1,word)
print("the count of the string length",a)

