#input='10110101010100100001000111000111'
input='00000010100101000001111010011100'
revstr=input[::-1]
print(revstr)
output=bin(int(revstr,2))
print(output)
op = output[2:]
print(op)
op2 = int(op,2)
print(op2)

