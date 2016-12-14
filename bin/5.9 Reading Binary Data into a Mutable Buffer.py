'''
Title    -  Reading Data into a Mutable Buffer   
Problem  -  Read binary data directly into a mutable buffer without any 
              intermediate copying.   Mutate data in place and write it 
              it back out to a file  
'''

# readinto()
# Reads data into a mutable array
import os.path 
def read_into_buffer(filename):
  buf = bytearray(os.path.getsize(filename))
  with open(filename, 'rb') as f:
    f.readinto(buf)
  return buf
# Write a sample file 
with open('sample.bin', 'wb') as f:
  f.write(b'Hello World')
buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'Hallo'
print(buf)
with open('newsameple.bin', 'wb') as f:
  print(f.write(buf))

print('\n!---SECTION---\n')

# readinto()
# Can fill any preallocated array of data  
# Includes arrays created from array module or libraries such as numpy 
# fills the contents of an existing buffer rather than allocating new objs
#   and returning
#   avoid making extra memory allocations
# always check return code, number of bytes read, do not want the supplied 
#   buffer to be smaller or truncation / corruption could occur
record_size = 32 # size of each record (adjust value)
buf = bytearray(record_size)
with open('sample.bin', 'rb') as f:
  while True:
    n = f.readinto(buf)
    if n < record_size:
      break
    # Use the contents of buf 
    print(n)

print('\n!---SECTION---\n')

# memoryview()
# lets you make zero-copy slices of an existing buffer & change its contents 
print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
print(m2[:])
print(buf)

print('\n!---SECTION---\n')
