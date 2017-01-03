'''
Title    -  Wrapping an Existing File Descriptor as a File Object  
Problem  -  Have an integer file descriptor corresponding to an already open I/O channel 
            on the OS (file, pipe, socket, etc).  
            Want to wrap a higher-lievel Python file object around it
'''

# file descriptor
# an integer handle assinged by OS to refer to some kind of system I/O channel 
# can wrap python file object around it using open() function 
# supply the integer file descriptor as the first arg instead of filename 

# Open a low-level file descriptor 
import os 
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a file 
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

print('\n!---SECTION---\n')

# when high-level object is closed or destroyed
# underlying file descriptor is closed
# if do not want supply closefd=False arg to open()
f = open(fd, 'wt', closefd=False)

print('\n!---SECTION---\n')

# signature 
# expose underlying signature of the wrapped function 
from inspect import signature
print(signature(countdown))