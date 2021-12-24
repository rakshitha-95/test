'''Python3 program to find the length  of the longest substring without repeating characters'''
def distinct(string,i,j):
    visited=[0]*(26)
    for k in range(i,j+1):
        if(visited[ord(string[k])-ord('a')]==True):
            return False
        visited[ord(string[k])-ord('a')]=True
    return True

# Returns length of the longest substring with all distinct characters.
def longestUniqueSubstr(string):
    n=len(string)
    res=0
    for i in range(n):
        for j in range(i,n):
            if (distinct(string,i,j)):
                res=max(res,j-i+1)
    return res
string="mynameisrakshitha"
print("the input is :",string)
len=longestUniqueSubstr(string)
print("the length of the longst substring is : ",len)