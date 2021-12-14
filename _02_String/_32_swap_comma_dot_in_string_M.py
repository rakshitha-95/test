'''Swap comma and dot in a string'''

def Replace(str1):
    maketrans=str1.maketrans
    final=str1.translate(maketrans(',.','.,',''))
    return final

str1="rakshitha.r.gowda,varun.k.h,vinith.r.gowda"
print(Replace(str1))

