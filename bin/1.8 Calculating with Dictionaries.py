'''
Title    -  1.7 Keeping Dictionaires in Order
Problem  -  Perform clcs on a dictionary of data (min, max, sort, etc)
Solution -  Use OrderedDict from Collection module to preserve the original 
              insertion order of data when iterating
'''

prices =  {
  'ACME': 45.23,
  'AAPL': 612.79,
  'IBM':  205.55,
  'HPQ':  32.70,
  'FB':   10.75
}

# Use zip() to invert keys and vaules of a dictionary
# zip creates an iterator that can only be used once 
#(can only use min, max, or sorted on a var).  can't reaccess var
min_price = min(zip(prices.values(), prices.keys()))
print('Minimum Price:', min_price)
max_price = max(zip(prices.values(), prices.keys()))
print('Maximum Price:', max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print('Sorted:', prices_sorted)

# without zip only processes keys:
print('Min:', min(prices))
print('Max:', max(prices))

# need values method to calc Values
print('Min:', min(prices.values()))
print('Max:', max(prices.values()))

# Use a key function to min() or max()
print('Min:', min(prices, key= lambda k: prices[k]))
print('Max:', max(prices, key= lambda k: prices[k]))

min_value = prices[min(prices, key=lambda k: prices[k])]
print('Minimum Price:', min_price)
