'''
Title    -  Taking a Slice of an Iterator  
Problem  -  Want a slice of an iterator, but normal slicing operator doesn't work  
Solution -  Use itertools.islice() to slice iterators & generators
'''

def count(n):
  while True:
    yield n 
    n += 1

c = count(0)
# Can't slice without an error 
# c[10:20]
# Use islice() 

# iterators & generators can't normally be sliced
#   no info about lenght & they don't implement indexing
# islice() produces desired iteration
#   consumes & discards items based on slice indexes
# since it's an iterator, can't rewind once islice() is executed
import itertools
for x in itertools.islice(c, 10, 20):
  print(x)

print('\n!---SECTION---\n')

