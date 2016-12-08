'''
Title    -  4.3 Creating New Iteration Patterns with Generators  
Problem  -  Want to implement a custom iteration pattern that's different than the 
              the built-in functions (range(), reversed(), etc) 
Solution -  Define a generator function
'''

def frange(start, stop, increment):
  x = start 
  while x < stop:
    yield x 
    x += increment 
for n in frange(0,4,.5):
  print(n)
print(list(frange(0,1,.125)))

# yield statemetn turns a function into a generator 
# generator only run in response to iteration
def countdown(n):
  print('Starting to count from', n)
  while n > 0:
    yield n
    n -=1
  print('Done!')
# Create generator, no ouput appears
c = countdown(3)
print(c)
# Run to first yield & emit a value 
print(next(c))
# Run to next yield 
print(next(c))
# Run to next yield 
print(next(c))
# Run to next yield (iteration stops)
print(next(c))