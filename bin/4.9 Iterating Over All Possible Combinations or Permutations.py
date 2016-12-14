'''
Title    -  Iterating over All Possible Combinations or Permutations  
Problem  -  Iterate over all possible combinations or permuations in a collection of items 
'''

# Itertools.permutations()
# Takes a collections of items and produces a seq of tuples that rearranges all of the 
#   items into all possible permutations 
# Does not consider order of elements (ie - (a,b) is the same as (b,a))
items = ['a', 'b', 'c']
from itertools import permutations 
for p in permutations(items):
  print(p)

# optioonal length arg to shorten length of iterable 
for p in permutations(items, 2):
  print(p)

print('\n!---SECTION---\n')

# itertools.combinations()
# Produce a seq of combinations of items taken from input 
# takes length option 
from itertools import combinations
for c in combinations(items, 3):
  print(c)
for c in combinations(items, 2):
  print(c)
for c in combinations(items, 1):
  print(c)

print('\n!---SECTION---\n')

# itertools.combinations_with_replacement()
# allows the same item to be chosen more than once
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
  print(c)

print('\n!---SECTION---\n')

