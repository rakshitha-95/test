'''find the length of the longest string'''

len_str = ['i am rakshitha','i am from rajajinagar','i have joined mcs']
res = max(len(ele) for ele in len_str)
print("Length of longest string:",res)



"Length of lonest string "
max_len = 0
for ele in len_str:
    if len(ele)>max_len:
        max_len = len(ele)
        res = ele
print(res)
#using functions
def Lon_str1(str1,max_len=0):

    for ele in str1:
        if len(ele) > max_len:
            max_len=len(ele)
            res1=max_len

    print("the longeststring" ,res1)

str1=['qwwe','xcvbnm','imhntgdc','qwertyasdj ']
Lon_str1(str1)
#using oops
class Lonstrg:

    def lon_str1(self,str1):
        self.str1=str1

        max_len=0
        for ele in str1:
            if len(ele) > max_len:
                max_len=len(ele)
                res=max_len
        return res
str1=[]
for i in range(4):
    st=input("enter the string")
    str1.append(st)

l=Lonstrg()

length=l.lon_str1(str1)
print("the longest length is ",length)





