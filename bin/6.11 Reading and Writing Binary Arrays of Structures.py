'''
Title    -  Reading & Writing Binary Arrays of Structures  
Problem  -  Want to read or write data encoded as binary array of uniform 
            structures into Python tuples
'''

# struct module  
# writes a list of Python tuples out to a binary file 
# encoding each tuple as a structure using struct 
from struct import Struct
def write_records(records, format, f):
  '''
  Write a seq of tuples to a binary file of structures 
  '''
  record_struct = Struct(format)
  for r in records:
    f.write(record_struct.pack(*r))
records = [ (1, 2.3, 4.5),
            (6, 7.8, 9.0),
            (12, 13.4, 56.7) ]
with open('data.b', 'wb') as f:
  write_records(records, '<idd', f)

print('\n!---SECTION---\n')

# Read the file incrementally in chunks 
def read_records(format, f):
  record_struct = Struct(format)
  chunks = iter(lambda: f.read(record_struct.size), b'')
  return (record_struct.unpack(chunk) for chunk in chunks)
with open('data.b', 'rb') as f:
  for rec in read_records('<idd', f):
    print(rec)

print('\n!---SECTION---\n')

# read entire file into a byte string with a single read & convert it 
# piece by piece 
def unpack_records(format, data):
  record_struct = Struct(format)
  return (record_struct.unpack_from(data, offset)
          for offset in range(0, len(data), record_struct.size))
with open('data.b', 'rb') as f:
  data = f.read()
for rec in unpack_records('<idd', data):
  print(rec)

print('\n!---SECTION---\n')

# new structure, declare with Struct 
# Little endian 32b int, 2 double precision floats 
# < byte ordering
# d structure code 
record_struct = Struct('<idd')

print('\n!---SECTION---\n')

# size() 
# contains teh size of the structure in bytes 
# pack() & unpack() 
# pack & unpack binary data 
print(record_struct.size)
s = record_struct.pack(1,2.0,3.0)
print(record_struct.unpack(s))

print('\n!---SECTION---\n')

# Struct instance
# format code specified once & operations grouped together & easier to maintain
# read_records()
# iter() 
# iterator that returns a fixed sized chunk 
# returns a specific value stops 
f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
print(chunks)
for chk in chunks:
  print(chk)

print('\n!---SECTION---\n')

def read_records(format, f):
  record_struct = Struct(format)
  while True:
    chk = f.read(record_struct.size)
    if chk == b'':
      break
    yield record_struct.unpack(chk)
  return records 

print('\n!---SECTION---\n')

# useful for extracting binary data from a larger binary array 
# no temporary obj or memory copies 
# pass byte string (or array) along with a byte offset 
def unpack_records(format, data):
  record_struct = Struct(format)
  return (record_struct.unpack(data[offset:offset + record_struct.size])
          for offset in rage(0, len(data), record_struct.size))

print('\n!---SECTION---\n')

from collections import namedtuple
Record = namedtuple('Record', ['kind','x','y'])
with open('data.b', 'rb') as f:
  records = (Record(*r) for r in read_records('<idd', f))
for r in records:
  print(r.kind, r.x, r.y)