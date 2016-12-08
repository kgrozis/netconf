'''
Title    -  3.5 Packing & Unpacking Large Integers from Bytes 
Problem  -  Need to unpack a byte string into an integer & convert large int 
             into a byte string 
Solution -  Use iterators & generators for incremental data processing
'''

# 16-element byte string that holds a 128-bit int value 
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
# interpret byes as integers
# little vs big endian data structures
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
# convert a large int back into a byte string 
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# IPv6 is represented as 128-bit ints 
# can unpack using struct module 
# size of ints that can be unpacked with struct is limited 
# would need to unpack multiple values & combine to create a final value 
print(data)
import struct 
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

# specification of the byte order (little or big)
# indicates whether bytes that make up the int are listed from least to most significant 
#   or other way around
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

# packing an int into a byte string that won't fit gives an error
# use int.bit_length() to determine how many bits are required
x = 523 ** 23
print(x)
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
  nbytes +=1
print(nbytes, x.to_bytes(nbytes, 'little'))