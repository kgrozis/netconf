'''
Title    -  Making Temporary Files & Directories  
Problem  -  Need to create a temp file or directory for use when your program executes 
            Afterwards, posibbly want the file or directory to be destroyed  
'''

# tempfile.TemporaryFile
from tempfile import TemporaryFile
# w+t = text mode 
# w+b = binary mode 
# simualtaneously supports write & read 
# accepts same args as open()
#   encoding='utf-8', errors='ignore'
# TemporaryFile is unamed 
with TemporaryFile('w+t') as f:
  # Read / Write to the file 
  f.write('Hello World\n')
  f.write('Testing\n')
  # Seek back to beginning & read the data 
  f.seek(0)
  data = f.read()
  print('Data Var:\n' + data)
# Temporary file is destroyed 

print('\n!---SECTION---\n')

f = TemporaryFile('w+t')
# Use the tempopary file 
f.write('Hello World\n')
f.write('Testing\n')
f.seek(0)
data = f.read()
print('Data Var:\n' + data)
f.close()
# File is destroyed 

print('\n!---SECTION---\n')

# NamedTemporaryFile() 
from tempfile import NamedTemporaryFile
# creates a named temporary file 
with NamedTemporaryFile('w+t') as f:
  # calls name and prints 
  print('filename is:' + f.name)
  f.write('Hello World\n')
  f.write('Testing\n')
  f.seek(0)
  data = f.read()
  print('Data Var:\n' + data)

print('\n!---SECTION---\n')

# tempfile.TemporaryDirectory()
from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
  # Creates a named directory 
  # calls Temporary Directory name and path 
  print('dirname is:', dirname)
  # Use the directory 
# Direcotry & all contents destroyed

print('\n!---SECTION---\n')

# mkstemp()
# mkdtemp()
import tempfile 
# returns raw OS file descriptor 
# must turn it into a proper file & clean up 
print(tempfile.mkstemp())
print(tempfile.mkdtemp())
# gives file location 
print(tempfile.gettempdir())

print('\n!---SECTION---\n')

# can override defaults & name 
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt, dir='/tmp')
print(f.name)