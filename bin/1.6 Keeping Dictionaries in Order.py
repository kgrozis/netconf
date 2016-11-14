'''
Title    -  1.7 Keeping Dictionaires in Order
Problem  -  Create a dictionary and control the order of items when iterating 
              or serializing
Solution -  Use OrderedDict from Collection module to preserve the original 
              insertion order of data when iterating
'''

from collections import OrderedDict

# OrderedDict useful when you want to build a mapping later you want serialize or encode
# into a different format.
# Example: Keep the order of JSON encoding
# Internally maintains a doublely linked list that orders keys according to insertion order
# New item appended to list
# If there is a reassignment of a key the order does not change
# Twice the size of a normal Dictionary
from collections import defaultdict

d = OrderedDict()
d['foo']  = 1
d['bar']  = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
  print(key, d[key])

import json
print(json.dumps(d))
