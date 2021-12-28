'''using with statement to open a file'''
with open('sample.txt','r') as f:
    for line in f:
        print(line)
f.close()