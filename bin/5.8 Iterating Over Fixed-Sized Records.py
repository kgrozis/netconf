'''
Title    -  Iterating over Fixed Sized Records 
Problem  -  Iterate over a file by bytes instead of lines. 
              a collection of fixed-sized records or chunks
Solution -  Use iter() function & functools.partial()
'''

from functools import partial
# fixed size chucks of 32B until EoF 
# last record maybe <32B
RECORD_SIZE = 32
# file must be open in read binary mode 
with open('/etc/passwd', 'rb') as f:
  # iter() creats an iterator if you pass a callable & a sentinel value 
  #   partial() is callable that reads fixed # of bytes 
  #   b'' is sentinel that gets returned from each read 
  records = iter(partial(f.read, RECORD_SIZE), b'')
  for r in records:
    print(r)

print('\n!---SECTION---\n')

