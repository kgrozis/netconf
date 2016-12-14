'''
Title    -  Reading & Writing Compressed Datafiles  
Problem  -  Read or write data in a file with gzip or bz2 compression   
Solution -  Use gzip and bz2 modules 
'''

# gzip compression
import gzip
text = 'Test 123\nTest 456\n'
with gzip.open('somefile.gz', 'wt') as f:
  f.write(text)

with gzip.open('somefile.gz', 'rt') as f:
  text = f.read()

print(text)

print('\n!---SECTION---\n')

# bz2 compression
import bz2
text = 'Test 789\nTest 101112\n'
with gzip.open('somefile.bz2', 'wt') as f:
  f.write(text)

with gzip.open('somefile.bz2', 'rt') as f:
  text = f.read()

print(text)

# use rb or wb to work with binary files 
# if you don't specify a mode.  default is binary

print('\n!---SECTION---\n')

# specifying compresession level 
# default level is 9
# lower levels offer better performance with less compression 
text = 'Test 131415\nTest 161718\n'
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
  f.write(text)

with gzip.open('somefile.gz', 'rt') as f:
  text = f.read()

print(text)

print('\n!---SECTION---\n')

# Can layer gzip.open() & bz2.open() when opening a binary file 
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
  text = g.read()

print(text)