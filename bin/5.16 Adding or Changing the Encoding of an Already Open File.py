'''
Title    -  Adding or Changing the Encoding of an Already Open File   
Problem  -  
'''

# io.TextIOWrapper() 
# add Unicode encoding/decoding to an existing file object
# that's opened in binary mode  
from urllib.request import urlopen 
from io import TextIOWrapper
u = urlopen('http://www.python.org')
f = TextIOWrapper(u, encoding='utf-8')
text = f.read()

print('\n!---SECTION---\n')

# detach()
# remove the existing text encoding layer
# replace it with a new one 
# sys.stdout 
import sys 
print(sys.stdout.encoding)
# breaks output of a terminal
# sys.stdout = TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
# print(sys.stdout.encoding)

print('\n!---SECTION---\n')

# I/O 
f = open('sample.txt', 'w')
# text 
print(f)
# binary 
print(f.buffer)
print(f.buffer.raw)

print('\n!---SECTION---\n')

# change encoding layer
f = TextIOWrapper(f.buffer, encoding='latin-1')
print(f)
# ValueError: I/O operation on closed
# f is destroyed & underlying file is destroyed
# f.write('Hello')

print('\n!---SECTION---\n')

# detach() 
# disconnects the topmost layer of a file 
# returns the next lower layer
# toplayer will no longer be usable 
f = open('sample.txt', 'w')
print(f)
b = f.detach()
print(b)
# ValueError: underlying buffer has been destroyed
# f.write('hello')

print('\n!---SECTION---\n')

# change top layer
f = TextIOWrapper(b, encoding='latin')
print(f)
# change line handling, error policy, & other aspects of file handling
# sys.stdout = TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
# print('Jalape\u00f1o')
# Terminal cannot handle
