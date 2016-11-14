'''
Title    -  1.17 Extracting a Subset of a Dictionary
Problem  -  Make a dictionary that is a subset of another dictionary
Solution -  Use a dictionary comprehension
'''

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key: value for key, value in prices.items() if value > 200 }
print('p1:', p1)

# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key: value for key, value in prices.items() if key in tech_names }
print('p2:', p2)

# create a seq of tuples and passing them to dict() func to create a subset
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print('p3:', p3)

# dict comprehensions are more readible and runs quicker
p4 = { key: prices[key] for key in prices.keys() & tech_names }
print('p4:', p4)