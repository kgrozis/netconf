'''
Title    -  Decoding & Encoding Hexadecimal Digits 
Problem  -  Need to decode a string of hex digits into a byte string or 
            encode a byte string as hex 
'''

# binascii module
# decode or encode a raw string of hex digits 
# initial byte string 
s = b'hello'
# encode as hex 
import binascii 
h = binascii.b2a_hex(s)
print(h)
# decode back to bytes 
print(binascii.a2b_hex(h))

# base64 module 
# similar functionality to binascii 
import base64 
h = base64.b16encode(s)
print(h)

print('\n!---SECTION---\n')

# base64 module 
# similar functionality to binascii 
import base64 
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))

print('\n!---SECTION---\n')

# case folding
# base64 operates in uppercase hex letters
# binascii works with either
# output produced by encoding is always a byte string 
h = base64.b16encode(s)
print(h)
print(h.decode('ascii'))

print('\n!---SECTION---\n')
