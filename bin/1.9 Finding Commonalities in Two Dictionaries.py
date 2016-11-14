'''
Title    -  1.9 Finding Commonalities in Two Dictionaries
Problem  -  Want to find out what is common between 2 dictionaries
Solution -  Use zip() to invert order
'''

a = {
  'x' : 1,
  'y' : 2, 
  'z' : 3
}

b = {
  'w' : 10,
  'x' : 11,
  'y' : 2
}

# Find keys in common
print('Common keys:', a.keys() & b.keys())

# Find keys in 'a' that are not in 'b'
print('Not keys:', a.keys() - b.keys())

# Find (key, value) pairs in common
print('Common keys & values', a.items() & b.items())

# Use these operations to alter or filter dictionary content 
# Make a new dictionary with certain keys removed
# Dictionary comprehension
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
for key in c.keys():
  print('Key:', key, ', Item:', c[key])