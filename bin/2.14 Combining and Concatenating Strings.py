'''
Title    -  2.14. Combining & Concatenating Strings 
Problem  -  Want to combine small strings together into large strings 
Solution -  Use join() method 
'''

# join is specified as a string operator even though you use it on list, tuples, files, sets, or generators 
# processor efficent
# runs fast 
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print('.'.join(parts))
print(''.join(parts))

# If you're cominbing a small number of strings use + operator
# processor inefficent
# runs slow
a = 'Is Chicago'
b = 'Not Chicago'
print(a + ' ' + b)

# can use + operator with formatting options
print('{} {}'.format(a,b))

# Can combine strings by placing them adjacent.  Don't need + operator
a = 'Hello' 'World'
print(a)

# Converstion of data to strings & conatenaton at same time using a generator
data = ['Acme', 50, 91.1]
print(','.join(str(d) for d in data))

# Make contatenation as simple as possible
c = 'test'
print(a,b,c, sep=':')

# build ouput from lots of small string use a generator function with yield
def sample():
  yield 'is'
  yield 'Chicago'
  yield 'Not'
  yield 'Chicago?'
text = ' '.join(sample())
print(text)
# redirect fragements to i/o 
# for part in sample():
#   f.write(part)
