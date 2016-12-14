'''
Title    -  Iterating over the Index-Value Pairs of a Seq 
Problem  -  Iterate over a seq, but would like to keep track of which element 
              of the seq is currently being processed
'''

# built-in enumerate()
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
  print(idx, val)

# enumerate start argument 
# specify starting number of index
for idx, val in enumerate(my_list, 1):
  print(idx, val)
# Good to use files.  Keeps track of line associated with error 
def parse_data(filename):
  with open(filename, 'rt') as f:
    for lineno, line in enumerate(f, 1):
      fields = line.split()
      try:
        count = int(fields[1])
      except ValueError as e:
        print('Line {}: Parse error: {}'.format(lineno,e))
parse_data('somefile.txt')

print('\n!---SECTION---\n')

# enumerate()
# keeps track of the offset into a list for occurences of certain values 
# map words in a file to lines in which they occur
'''
word_summary = defaultdict{[]}
with open('somefile.txt') as f:
  lines = f.readlines()
for idx, line in enumerate(lines):
  # Create a list of words in current line 
  words = [w.strip().lower() for w in line.split()]
  for word in words:
    word_summary[word].append(idx)
'''

print('\n!---SECTION---\n')

# enumerate()
# shortcut where you need a counter var
# calls next() and returns a tuple of index & value 
'''
lineno = 1
for line in f:
  # process line
  lineno += 1
# vs
for lineno, line in enumerate(f):
  # process line
'''

print('\n!---SECTION---\n')

# Unpacking tuples with enumerate()
# need to use (,) with unpacking to expect the data struct 
# correct:
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
for n, (x, y) in enumerate(data):
  print(n, (x,y))
# unpack error:
'''
for n, x, y in enumerate(data):
  print(n, x, y)
'''