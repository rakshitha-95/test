#displaying marks and names
import re
str='Rakshitha got 70 marks,Varun got 80 marks,where Vini got 67 marks '
#extract only marks having 2 digits
marks=re.findall('\d{2}',str)
print(marks)
#extract names starting with acapital letter
#and remainning alphabetic characters
names=re.findall('[A-Z][a-z]*',str)
print(names)