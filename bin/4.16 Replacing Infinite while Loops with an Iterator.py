'''
Title    -  Replacing Infinite while Loops with an Iterator  
Problem  -  Using while loop to iteratively process data 
            Involves a function or some kind of unusual test condition 
            Doesn't fall into the usual iteration pattern 
'''

# I/O 
CHUNKSIZE = 8192 
def reader(s):
  while True:
    data = s.recv(CHUNKSIZE)
    if data == b'':
      break 
    process_data(data)

print('\n!---SECTION---\n')

# replace with iter()
def reader(s):
  for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
    process_data(data)

print('\n!---SECTION---\n')

# Files 
import sys 
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
  n = sys.stdout.write(chunk)

print('\n!---SECTION---\n')

# iter() accepts a zero-arg callable & sentinel value as inputs
# creates iterator that repeatedly calls supplied callable
# iterates until it returns the value of sentinel 