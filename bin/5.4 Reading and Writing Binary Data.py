'''
Title    -  5.4. Reading & Writing Binary Data  
Problem  -  Need to read or write binary data 
Solution -  Use open() with mode rb or wb 
'''

# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
  data = f.read()
  print(data)

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
  f.write(b'Hello World')

print('\n', '-'*25, '\n')

# indexing & iteration return integer byte values 
# instead of byte strings
print('Text String:')
t = 'Hello World'
print(t[0])
for c in t:
  print(c)
print('Byte String:')
b = b'Hello World'
print(b[0])
for c in b:
  print(c)

print('\n', '-'*25, '\n')

# when reading & writing binary file must decode or encode it
with open('somefile.bin', 'rb') as f:
  data = f.read(16)
  text = data.decode('utf-8')
  print(text)
with open('somefile.bin', 'wb') as f:
  text = 'Hello World'
  f.write(text.encode('utf-8'))

print('\n', '-'*25, '\n')

# objects such as arrays and C structs
# can be used for writing without conversion
import array
nums = array.array('i', [1,2,3,4])
with open('data.bin', 'wb') as f:
  f.write(nums)
# can directly read binary with readinto() method 
a = array.array('i', [0,0,0,0,0,0,0,0])
with open('data.bin', 'rb') as f:
  f.readinto(a)
print(a)
