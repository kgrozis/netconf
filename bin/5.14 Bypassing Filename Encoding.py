'''
Title    -  Bypassing Filename Encoding  
Problem  -  Want to perform file I/O ops using raw filenames that have 
            not decoded or encoded according to the default filename encoding   
'''

# sys.getfilesystemencoding()
# filename are encoded & decoded according to the text encoding 
import sys
print(sys.getfilesystemencoding())

print('\n!---SECTION---\n')

# bypass encoding 
# write a file using a unicode filename 
print('unicode filename')
with open('jalepe\xf1o.txt', 'w') as f:
  f.write('Spicy!')

print('\n!---SECTION---\n')

# directory listing (decoded)
import os 
print('ls:', os.listdir('.'))

print('\n!---SECTION---\n')
  
# directory listing (raw)
print(os.listdir(b'.'))     # Note: byte string

print('\n!---SECTION---\n')

# open file with raw filename 
with open(b'jalepen\xcc\x83o.txt') as f:
  print(f.read())

print('\n!---SECTION---\n')

