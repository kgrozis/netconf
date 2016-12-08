'''
Title    -  Defining Generator Functions with Extra State  
Problem  -  Define a generator function that expose extra state to user 
Solution -  Implement as a class with __iter__() method 
'''

from collections import deque
class linehistory:
  def __init__(self, lines, histlen=3):
    print('__init__')
    self.lines = lines
    # create history instance with a circular buffer of 3
    self.history = deque(maxlen=histlen)
  def __iter__(self):
    print('__iter__')
    for lineno, line in enumerate(self.lines,1):
      self.history.append((lineno, line))
      print('yield:', lineno)
      yield line 
  def clear(self):
    print('clear')
    self.history.clear()

print('\n!---SECTION---\n')

# Use linehistory like a normal generator function
# Since it is an instance, you can access internal attributes
# Can access state using history 
# Can clear state using clear() method
with open('somefile.txt') as f:
  lines = linehistory(f)
  # call __iter__
  for line in lines:
    if 'python' in line:
      # access history buffer 
      for lineno, hline in lines.history:
        print('{}:{}'.format(lineno, hline), end='')

print('\n!---SECTION---\n')

# Need another step if you drive loop without using a for loop
f = open('somefile.txt')
lines = linehistory(f)
# call iter() first then start iterating
it = iter(lines)
next(it)
next(it)