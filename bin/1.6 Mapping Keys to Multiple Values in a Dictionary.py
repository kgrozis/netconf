'''
Title    -  1.6 Mapping Keys to Multiple Values in a Dictionary
Problem  -  Want to make a dictionary that maps keys to more than one value 
              (a so-called 'multidict')
Solution -  Dictionaries map a key to a single value.  Need to store the 
               multiple values in another container such as a list or set
'''

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
# Use a list if you want to preserve the insertion order of the items 
# Use a set if you want to eliminate duplicates and don't care about order

# defaultdict automatically initializes the 1st value so you can focus on adding items
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = {} # A regular dictionary
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)