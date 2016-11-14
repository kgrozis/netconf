'''
Title    -  1.15 Grouping Records Together Based on a Field
Problem  -  Have data inside of a seq and need to extract values or reduce
              the seq using some criteria
Solution -  Use a list comprehension
'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print('List Comprehension +', [n for n in mylist if n > 0])
print('List Comprehension -', [n for n in mylist if n < 0])

# List comps can produce large results
# Use generator expr to produce the filtered values iteratively
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
  print(x)

# Filtering criteria cannot be easily expressed in list comp or generator expr 
# Put filtering code into its own function using built-in filter() method 
values = values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
  try:
    x = int(val)
    return True
  except ValueError:
    return False 

# filter() creates an iterator 
# must use list() method create a list with the results
ivals = list(filter(is_int, values))
print('Ints:', ivals)

import math 
# Using math to transform data in a list comprehension
print('Math List Comprehension', [math.sqrt(n) for n in mylist if n > 0])

# Using a conditional expr to filter within a list comp 
# if negative, the list comp replaces it with a zero
clip_neg = [n if n > 0 else 0 for n in mylist]
print('Clip Neg', clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print('Clip Pos', clip_pos)

# itertools.compress(), takes an iterable and a boolean selector seq
#   return output items that are True 
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# Make a list of all addresses where corresponding count value is greater than 5
from itertools import compress
more5 = [n > 5 for n in counts]
print('More5:,', more5)
# compress() function picks items corresponding to true values 
# compress() returns an iterator so need list() method on results
print('Compress', list(compress(addresses, more5)))
