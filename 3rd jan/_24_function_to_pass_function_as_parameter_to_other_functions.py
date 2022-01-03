'''functions can be passed as parameters to other functions'''
def display(fun):
    return 'hai'+fun
def message():
    return 'how are you?'
#call display() function and pass message() function
print(display(message()))