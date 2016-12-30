'''
Title    -  Iterating over Multi Seqs Simultaneously  
Problem  -  Want to iterate over the items contained in more than one seq at a time 
'''

# zip() 
# iteration stops whenever one of the input seq is exhuasted 
xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,15,62,99]
for x,y in zip(xpts,ypts):
  print(x,y)

print('\n!---SECTION---\n')

# creates an iterator that produces tuples(x,y)
a = [1,2,3]
b = ['w','x','y','z']
for i in zip(a,b):
  print(i)

print('\n!---SECTION---\n')

# itertools.zip_longest() 
# iterates until longest list complete 
from itertools import zip_longest
for i in zip_longest(a,b):
  print(i)
# default fill is 'None'
# fillvalue allows user-defined value 
for i in zip_longest(a,b, fillvalue=0):
  print(i)

print('\n!---SECTION---\n')

# zip()
# commonly used whenver a data pair is referenced together 
# list of column headers & column values 
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
# use zip to create a dictionary
s = dict(zip(headers,values))
# to produce output 
for name, val in zip(headers, values):
  print(name, '=', val)

print('\n!---SECTION---\n')

# zip() 
# passed more than 2 seq as input 
a = [1,2,3]
b = [10,11,12]
c = ['x','y','z']
for i in zip(a,b,c):
  print(i)

print('\n!---SECTION---\n')

# zip()
# zip creates an iterator as a result 
# can store values in a list 
print(zip(a,b))
print(list(zip(a,b)))