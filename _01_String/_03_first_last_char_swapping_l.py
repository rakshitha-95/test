'''first last character swapping'''
list=("my name is rakshitha")
start=list[0]
end=list[-1]
swapping_str=end+list[1:-1]+start
print(swapping_str)
#using functions
def swapping_string(str1):

    start=str1[0]
    end=str1[-1]
    swapping_str=end+str1[1:-1]+start
    print(swapping_str)

str1="my name is rakshitha"
swapping_string(str1)

#using oops
class Swap:
    def swapping_string(self,str1):
        self.str1=str1
        start = str1[0]
        end = str1[-1]
        swapping_str = end + str1[1:-1] + start
        return (swapping_str)

str1 = "my name is rakshitha"
s=Swap()
swap=s.swapping_string(str1)
print("the swapping of first and last character is :",swap)

