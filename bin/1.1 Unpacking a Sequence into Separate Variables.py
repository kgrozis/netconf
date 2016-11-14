'''
Title    -  1.1 Unpacking a Sequence into Separate Variables
Problem  -  Have an N-element tuple or seq that you would like to unpack into 
              a collection of N variables
Solution -  Any seq can be unpacked into bars using a simple assignement operation.
              The only requirement is that the # of vars and struct match the  seq
'''

# Tuple unpacking
p = (4, 5)
x, y = p
print('Var x:', x)
print('Var y:', y)

# List unpacking
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print('Date:', date)
name, shares, price, (year, mon, day) = data
print('Name:', name)
print('Year:', year)
print('Month:', mon)
print('Day:', day)

# Mismatch in elements.  Produces error
p = (4,5)
# Calling 3 elements when only 2 are present.
# Creates error
# x, y, z = p

# String unpacking
# Can unpack: iterable, tuples, lists, strings, files, iterators, generators 
s = 'Hello'
a, b, c, d, e = s
print('Char a:', a)
print('Char b:', b)
print('Char 3:', e)
 
# Use a throwaway var for unwanted values
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print('Shares:', shares)
print('Price:', price)