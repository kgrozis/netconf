'''
Title    -  Manipulating Pathnames  
Problem  -  Need to manipulate pathnames to find base filename, 
            directory name, absolute path, etc...  
'''

# os.path module  
# manipulate pathnames  
import os 
path = '/Users/kgrozis/Docker/netconf/bin/stocks.csv'

# os.path.basename()
# get the last component of the path 
print(os.path.basename(path))

print('\n!---SECTION---\n')

# os.path.dirname()
# get the directory name 
print(os.path.dirname(path))

print('\n!---SECTION---\n')

# os.path.join()
# join path components together 
print(os.path.join('tmp', 'data', os.path.basename(path)))

print('\n!---SECTION---\n')

# os.path.expanduser()
# expand the user's home directory 
path = '~/Docker/netconf/bin/stocks.csv'
print(os.path.expanduser(path))

print('\n!---SECTION---\n')

# os.path.splitext()
# split the file extension 
print(os.path.splitext(path))

print('\n!---SECTION---\n')

