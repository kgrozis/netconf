'''
Title    -  Decoding & Encodng Base64 
Problem  -  decode or encode binary data using base64 encoding 
'''

# b64encode 
# Some byte data 
s = b'hello'
import base64
# encode as base64 
a = base64.b64encode(s)
print(a)

print('\n!---SECTION---\n')

# b64decode 
base64.b64decode(a)
print(a)

print('\n!---SECTION---\n')

# only use on byte oriented data like byte strings & arrays 
# unicode text strings only contain ASCII chars
a = base64.b64encode(s).decode('ascii')
print(a)

print('\n!---SECTION---\n')

