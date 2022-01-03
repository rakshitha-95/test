'''functions can return othr functions'''
def display():
    def message():
        return 'how are u?'
    return message

fun=display()
print(fun())