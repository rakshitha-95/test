class Space:
    def remove_space(self):
        n = input("Enter your number:").split(" ")
        join_str = ",".join(n)
        return join_str

s=Space()
removespace=s.remove_space()
print("removed space of the string",removespace)