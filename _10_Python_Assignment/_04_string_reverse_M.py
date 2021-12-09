class Prgm:
    def reverse(self):
        try:
            string1 = int(input('enter a string:'))
            if len(string1) % 4 ==0:
                print(''.join(reversed(string1)))
        except Exception as e:
            print('the exception is',e)
obj=Prgm()
obj.reverse()