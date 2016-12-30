'''
Title    -  Getting a Direcotry Listing   
Problem  -  Geta list of the files contained in a dir on the filesystem  
'''

# os.listdir
# obtains list of files in dir
# raw dir listing: all files, subdirs, symbolic links 
import os 
names = os.listdir('/Users/kgrozis')
print('all\n',names)

print('\n!---SECTION---\n')

# os.path.isfile
# filter dirs
import os.path 
# Get all regular files 
names = [name for name in os.listdir('/Users/kgrozis')
         if os.path.isfile(os.path.join('/Users/kgrozis', name))]
print('files:\n', names)

print('\n!---SECTION---\n')

# os.path.isdir
# Get all dirs 
dirnames = [name for name in os.listdir('/Users/kgrozis')
         if os.path.isdir(os.path.join('/Users/kgrozis', name))]
print('directories:\n',dirnames)

print('\n!---SECTION---\n')

# startswith() or endswith()
pyfiles = [name for name in os.listdir('/Users/kgrozis')
           if name.endswith('.py')]
print('Python:\n', pyfiles)

print('\n!---SECTION---\n')

# glob or fnmatch
# filename matching 
import glob
pyfiles = glob.glob('Users/kgrozis/*.py')
print('glob:\n', pyfiles)

from fnmatch import fnmatch 
pyfiles = [name for name in os.listdir('/Users/kgrozis')
           if fnmatch(name, '*.py')]
print('fnmatch:\n', pyfiles)

print('\n!---SECTION---\n')

# os.stat()
# get file metadata like size, mod, etc...
pyfiles = glob.glob('*.py')

# size & mod date 
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
  print(name, size, mtime)

print('\n!---SECTION---\n')

# alternative metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
  print(name, meta.st_size, meta.st_mtime)