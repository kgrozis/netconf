'''
Title    -  Memory Mapping Binary Files
Problem  -  Memory map a binary file into a mutable byte array, 
            possibly for random access to its content or make in-place
            modifications
'''

# mmap()
# memory map files 
# open a file & memory map it in a portable manner 
import os
import mmap 
def memory_map(filename, access=mmap.ACCESS_WRITE):
  size = os.path.getsize(filename)
  fd = os.open(filename, os.O_RDWR)
  return mmap.mmap(fd, size, access=access)
size = 1000000
with open('data', 'wb') as f:
  f.seek(size-1)
  f.write(b'\x00')
m = memory_map('data')
print(len(m))
print('index 0:10:', m[0:10])
print('index 0:', m[0])

print('\n!---SECTION---\n')

# enumerate()
# keeps track of the offset into a list for occurences of certain values 
# map words in a file to lines in which they occur
'''
word_summary = defaultdict{[]}
with open('somefile.txt') as f:
  lines = f.readlines()
for idx, line in enumerate(lines):
  # Create a list of words in current line 
  words = [w.strip().lower() for w in line.split()]
  for word in words:
    word_summary[word].append(idx)
'''

print('\n!---SECTION---\n')

# enumerate()
# shortcut where you need a counter var
# calls next() and returns a tuple of index & value 
'''
lineno = 1
for line in f:
  # process line
  lineno += 1
# vs
for lineno, line in enumerate(f):
  # process line
'''

print('\n!---SECTION---\n')

# Unpacking tuples with enumerate()
# need to use (,) with unpacking to expect the data struct 
# correct:
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
for n, (x, y) in enumerate(data):
  print(n, (x,y))
# unpack error:
'''
for n, x, y in enumerate(data):
  print(n, x, y)
'''