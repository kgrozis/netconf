'''
Title    -  Skipping the First Part of an Iterable 
Problem  -  Want to discard for items of an iterable 
Solution -  Use functions in itertools module 
'''

# Supply itertools.dropwhile() with a function & iterable 
#  returned iterator discards first items 
with open('/etc/passwd') as f:
  for line in f:
    print(line, end='')

print('\n!---SECTION---\n')

# want to skip the initial comments 
from itertools import dropwhile 
with open('/etc/passwd') as f:
  for line in dropwhile(lambda line: line.startswith('#'), f):
    print(line, end='')

print('\n!---SECTION---\n')

# if you know exact number of lines you want to skip 
#   use itertools.islice()
from itertools import islice 
items = ['a', 'b', 'c', 1, 4, 10, 15]
# None arg tells islice that you want everything beyond 1st 3 items 
#   as opopose to only 1st 3 items
for x in islice(items, 3, None):
  print(x)

print('\n!---SECTION---\n')

# same code without itertools.dropwhile()
with open('/etc/passwd') as f:
  # logic to skip initial comments 
  while True:
    line = next(f, '')
    if not line.startswith('#'):
      break 
# process remaining lines 
  while line:
    # replace with useful processing 
    print(line, end='')
    line = next(f, None)

print('\n!---SECTION---\n')

# same code with itertools.islice()
# will discard first line comments & other comments  in body 
#   breaks use case 
with open('/etc/passwd') as f:
  lines = (line for line in f if not line.startswith('#'))
  for line in lines:
    print(line, end='')
