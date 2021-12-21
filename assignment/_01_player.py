'''Assignment Problem - player A and B playing a game, both players have given same string and both players have to make substring using
letters of string.B has to make words starting with consonants, A has to make words starting with vowels.
Count total no of substrings, if count of any player is greater then annouce it as winner.'''
import itertools
player_name="ab".lower()
length=len(player_name)
list1=[]
list2=[]
A_dict={}
B_dict={}

for i in range(1,length+1):
    list1.append(list(itertools.permutations(player_name,i)))
    for tup in list1:
        for element in tup:
            str1= "".join(element)
            list2.append(str1)
print(list2)
for players_name2 in list2:
    if players_name2[0] in ['a','e','i','o','u']:
        A_dict[players_name2]=A_dict.get(players_name2,0)+1
    elif players_name2 in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        B_dict[players_name2]=B_dict.get(players_name2,0)+1

print(A_dict)
print(B_dict)
if len(A_dict.values()) > len(B_dict.values()):
    print("A is winner - Length ",len(A_dict.values()))
else:
    print("B is winner - Length ", len(B_dict.values()))



