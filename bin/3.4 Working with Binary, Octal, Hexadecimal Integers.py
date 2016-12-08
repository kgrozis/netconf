'''
Title    -  3.4 Working with Binary, Octal, and Hexadecimal Integers 
Problem  -  Need to convert integers represented by binary, octal, or hexadecimal digits
Solution -  use bin(), oct(), hex()
'''

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

# use format() to remove 0b, 0o, or 0x
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# integers are signed and this carries to base notation 
x = -1234
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# need to produce an unsigned value 
# need to add max value to set the bit length 
# shows a 32-bit value 
x = -1234
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

# use int() to convert to a different base 
print(int('4d2', 16))
print(int('10011010010', 2))

# octal values 
import os
os.chmod('script.py',0o755)