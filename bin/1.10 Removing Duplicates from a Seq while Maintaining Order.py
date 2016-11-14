'''
Title    -  1.10 Removing Duplicates from a Sequence while Maintaining Order
Problem  -  Want to eliminate duplicate values in a seq, but preserve remaining items order
Solution -  Use set and a generator
'''

# Only for hashable datatypes
def dedupe(items):
  seen = set()
  for item in items:
    if item not in seen:
      yield item
      seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print('Minus dups:', list(dedupe(a)))

# for unhashable datatypes 
def dedupe(items, key=None):
  seen = set()
  for item in items:
    val = item if key is None else key(item)
    if val not in seen:
      yield item
      seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print('Minus dups:', list(dedupe(a, key=lambda d: (d['x'],d['y']))))
print('Minus dups:', list(dedupe(a, key=lambda d: d['x'])))

# set easily eliminates dups 
a = [1, 5, 2, 1, 9, 1, 5, 10]
print('With dups:', a)
print('Without dups:', set(a))
