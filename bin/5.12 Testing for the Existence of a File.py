'''
Title    -  Testing for Existence of a File  
Problem  -  Need to test whether or not a file or directory exists 
'''

# os.path.exists()
# tests the existence of a file or directory 

import os 
print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))

print('\n!---SECTION---\n')

# os.path.isfile()
# what kind of file it might be
# if file doesn't exist, it returns false 

# Is a regular file 
print(os.path.isfile('/etc/passwd'))

# Is a directory 
print(os.path.isdir('/etc/passwd'))

# Is a symbolic link 
print(os.path.islink('/usr/local/bin/python3'))

# get the file linked to 
print(os.path.realpath('/usr/local/bin/python3'))

print('\n!---SECTION---\n')

# os.path()
# get metadata (file size or mod date)
print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))

import time 
print(time.ctime(os.path.getmtime('/etc/passwd')))

print('\n!---SECTION---\n')

# beware of permissions
# os.path.getsize('~/kgrozis')