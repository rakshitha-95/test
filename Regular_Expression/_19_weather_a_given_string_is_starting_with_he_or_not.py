import re
str="hello world"
res=re.search(r"^He",str)
if res:
    print("strings stats with 'He'")
else:
    print("strings does not end with 'He'")