'''
Title    -  1.18 Mapping Names to Sequence Elements
Problem  -  Accessing lists or tuples elements by position & want more redible code.
              Like to be less dependent on position in structure by accessing teh elements by name
Solution -  Use collections.namedtuple().  Returns a sublclass of the std tuple type. 
              Feed it a type name and the fields you want.  It returns a class that you can
              instantiate, passing in values for fields you've defined
'''

from collections import namedtuple
# Tuple named Subscriber with fields: addr & joined
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)      # access full record
print(sub.addr) # access field in record
print(sub.joined)

# Support traditional tuple operations
print(len(sub))     # length
addr, joined = sub  # assign vars 
print(addr)
print(joined)

# references positional elements 
# makes code dependent on data structure
def compute_cost(records):
  total = 0.0
  for rec in records:
    total += rec[1] * rec[2]
  return total 

# namedtuple version without positional elements ref 
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
  total = 0.0
  for rec in records:
    s = Stock(*rec)
    # call by fields more flexible
    total += s.shares * s.price
  return total 

# can used namedtuple as a replacement for a dictionary.  dict require more space 
#   to store.  namedtuple is immutable
s = Stock('ACME', 100, 123.45)
print(s)
# Can't change attribute value
#s.shares=75

# Can change attribute with _replace() method or optional or missing fields 
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance 
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock 
def dict_to_stock(s):
  return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

