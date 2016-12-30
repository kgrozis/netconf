'''
Title    -  Iterating on Items in Separate Containers  
Problem  -  Need to perform same operation on many objects
              objects are in different containers 
              want to avoid loops 
              readible code 
'''

# itertools.chain()
# inputs list of iterables 
# returns an iterator that masks acting on multi containers 
from itertools import chain 
a = [1,2,3,4]
b = ['x','y','z']
for x in chain(a,b):
  print(x)

print('\n!---SECTION---\n')

# itertools.chain()
# perform operations on all of the items at once
# items are pooled into different working sets  

# Various working sets of items 
active_items = set()
inactive_items = set()

# Iterate over all items 
for item in chain(active_items, inactive_items):
  # Process items 
  print(item)

print('\n!---SECTION---\n')


