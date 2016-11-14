'''
Title    -  1.11 Naming a Slice
Problem  -  Don't want to do hardcoded slice indices
Solution -  Use named slices
'''

# Typical method of slicing
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print('Cost:', cost)

# Named slices
# Improves readibility
# slice() is a built-in obj that can be anywhere with a slice
SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
print('Cost:', cost)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)
print('Slice:',items[2:4])
print('Slice:',items[a])
items[a] = [10,11]
print('Items:',items)
del items[a]
print('Items:',items)

# slice() obj have start, stop, & step attributes 
a = slice(10, 50, 2)
print('start:', a.start)
print('stop:', a.stop)
print('step:', a.step)

# map a slice onto a seq of specific size by using its indicies slice
# returns a tuple (start, stop, step)
s = 'HelloWorld'
print('indices',a.indices(len(s)))
for i in range(*a.indices(len(s))):
  print(s[i])
