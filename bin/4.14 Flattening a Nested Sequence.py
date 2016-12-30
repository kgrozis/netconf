'''
Title    -  Flattening a Nested Seq  
Problem  -  Have a nested seq that you want to flatten into a single list of values  
'''

# yield from statement
# recursive generator function 
# Iterable()
from collections import Iterable 
def flatten(items, ignore_types=(str, bytes)):
  for x in items:
    # check if instance is iterable (ie - list)
    # ignores bytes that do not iterate correctly
    if isinstance(x, Iterable) and not isinstance(x, ignore_types):
      # emits all of its values as a subroutine 
      # output is single sequence without nesting
      yield from flatten(x)
    else:
      yield x 
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
  print(x)

print('\n!---SECTION---\n')

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
  print(x)

print('\n!---SECTION---\n')

# yield from statement
# generator that calls a generator 
def flatten(items, ignore_types=(str, bytes)):
  for x in items:
    if isinstance(x, Iterable) and not isinstance(x, ignore_types):
      # extra loop without yeild from statement
      for i in flatten(x):
        yield i
    else:
      yield x 
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
  print(x)

print('\n!---SECTION---\n')
  
print('\n!---SECTION---\n')



print('\n!---SECTION---\n')

