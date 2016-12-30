'''
Title    -  Reading Nested & Variable-Sized Binary Structures  
Problem  -  Need read comlicated binary-encoded data that contains a 
            collection of nested and/or variable sized records
            ie - images, video, etc...
'''

# sturct module 
# decode & encode binary data structures 
polys = [
          [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
          [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
          [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
        ]

import struct 
import itertools 
def write_polys(filename, polys):
  # Determine bounding box 
  flattened = list(itertools.chain(*polys))
  min_x = min(x for x, y in flattened)
  max_x = max(x for x, y in flattened)
  min_y = min(y for x, y in flattened)
  max_y = max(y for x, y in flattened)
  with open(filename, 'wb') as f:
    f.write(struct.pack('<iddddi',
                        0x1234,
                        min_x, min_y,
                        max_x, max_y,
                        len(polys)))
    for poly in polys:
      size = len(poly) * struct.calcsize('<dd')
      f.write(struct.pack('<i', size+4))
      for pt in poly:
        f.write(struct.pack('<dd', *pt))
# Call it with polygon data 
write_polys('polys.bin', polys)

print('\n!---SECTION---\n')

# struct.unpack()
# read back data 
def read_polys(filename):
  with open(filename, 'rb') as f:
    # Read the header 
    header = f.read(40)
    file_code, min_x, min_y, max_x, max_y, num_polys = \
        struct.unpack('<iddddi', header)
    polys = []
    for n in range(num_polys):
      pbytes, = struct.unpack('<i', f.read(4))
      poly = []
      for m in  range(pbytes // 16):
        pt = struct.unpack('<dd', f.read(16))
        poly.append(pt)
      polys.append(poly)
  return polys 
p = read_polys('polys.bin')
print(p)

print('\n!---SECTION---\n')

# struct module 
# unpack using a class 
class StructField:
  '''
  Descriptor representing a simple structure field 
  '''
  # descriptor to represent each structure field
  def __init__(self, format, offset):
    print('StructField.__init__()')
    self.format = format 
    self.offset = offset 
  # unpack a value from buffer w/o extra slices or copies
  def __get__(self, instance, cls):
    print('StructField.__get__()')
    if instance is None:
      return self 
    else:
      r = struct.unpack_from(self.format, instance._buffer, self.offset)
      return r[0] if len(r) == 1 else r 
# base class 
# accepts some byte data & stores it as the underlying memory buffer 
#   used by StructField
class Structure:
  def __init__(self, bytedata):
    self._buffer = memoryview(bytedata)
# Define a high-level class that mirrors the info found in the tables 
# Describes expected file format 
class PolyHeader(Structure):
  file_code = StructField('<i',0)
  min_x = StructField('<d', 4)
  min_y = StructField('<d', 12)
  max_x = StructField('<d', 20)
  max_y = StructField('<d', 28)
  num_polys = StructField('<i', 36)

f = open('polys.bin', 'rb')
phead = PolyHeader(f.read(40))
print(phead.file_code == 0x1234)

print('\n!---SECTION---\n')

print(phead.min_x)
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)

print('\n!---SECTION---\n')

