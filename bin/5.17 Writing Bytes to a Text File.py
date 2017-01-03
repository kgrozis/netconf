'''
Title    -  Writing Bytes to a Text File   
Problem  -  Write raw bytes to a file opened in text mode 
'''

# buffer
# write byte data to files underlying buffer 
import sys 
# sys.stout is allows pointed to text mode
# TypeError must be string not bytes
# sys.stdout.write(b'Hello\n')
sys.stdout.buffer.write(b'Hello\n')

print('\n!---SECTION---\n')

# Can use read from a text file 
# Text is built on top of a buffered binary-mode file
# buffer attribute points underlying file 