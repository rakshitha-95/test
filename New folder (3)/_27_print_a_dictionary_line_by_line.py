'''Print a dictionary line by line'''
students={'raksh':{'class':5,'roll_num':8},'varun':{'class':8,'rollnum':9}}
for i in students:
    print(i)
    for j in students[i]:
        print(j,':',students[i][j])