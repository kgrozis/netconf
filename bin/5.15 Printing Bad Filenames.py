'''
Title    -  Printing Bad Filenames  
Problem  -  Receive a directory listing
            Try to print filenames
            Crashes with a UnicodeEncodeError exception 
            and msg 'surrogates not allowed'
'''

import os
files = os.listdir('.')
print(files)

# try / except 
def bad_filename(filename):
  return repr(filename)[1:-1]
for filename in files:
  try:
    print(filename)
  except UnicodeEncodeError:
    print(bad_filename(filename))

print('\n!---SECTION---\n')

# reencode name 
def bad_filename(filename):
  temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
  return temp.decode('latin-1')
for name in files:
  try:
    print(name)
  except UnicodeEncodeError:
    print(bad_filename(name))


print('\n!---SECTION---\n')
