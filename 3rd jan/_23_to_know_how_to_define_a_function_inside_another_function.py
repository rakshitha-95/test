#define a function inside another function
def display(str):
    def message():
        return'How are U?'
    result=message()+str
    return result
#call display() function
print(display("rakshitha"))