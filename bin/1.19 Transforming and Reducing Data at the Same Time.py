'''
Title    -  1.19 Transforming & Reducing Data at the Same Time
Problem  -  Need to execute a reduction function (sum, min, max), but first
              need to transform or filter data
Solution -  Use a generator-expression argument
'''

# Calculate the sum of squares
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print('Sum of Squares:', s)

# Determin if any .py files exist in a directory 
import os
files = os.listdir('/Users/kgrozis/Python/Python Cookbook')
if any(name.endswith('.py') for name in files):
  print('There be python!')
else:
  print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure 
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print('Min Share:', min_shares)

# Don't need repeated parentheses
s = sum((x * x for x in nums)) # Pass generator-expr as argument 
s = sum(x * x for x in nums)

# Introduces an extra step & creates an extra list
# Bad for large data structures
# Generator transforms the data iteratively & more memory efficent
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
print('Sum:', s)

# reduction functions accessing a key argument
# Orignal: Returns 20
min_shares = min(s['shares'] for s in portfolio)
print('Min Share:', min_shares)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print('Min Share', min_shares)