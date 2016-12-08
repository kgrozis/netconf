'''
Title    -  4.1 Manually Consuming an Iterator   
Problem  -  Need to process items in an iterable, but don't want to use a for loop
Solution -  Manually consume an iterable use next() method 
              catch the StopIteraction exception 
'''

# StopIteration signals end of iteration
with open('/etc/passwd') as f:
  try:
    while True:
      line = next(f)
      print(line, end='')
  except StopIteration:
    pass

# instruct next() to return a terminating value 
with open('/etc/passwd') as f:
  while True:
    line = next(f, None)
    if line is None:
      break
    print(line, end='')

# for statement is typicallablely used to consume an iterable 
#   occasionally need more precise control of iteration mechanism 
#   need to know what's happening
items = [1, 2, 3]
# get the iterator 
it = iter(items)  # Invokes items.__iter__()
# run the iterator 
print('Iterate:', next(it)) # Invokes it.__next__()
print('Iterate:', next(it))
print('Iterate:', next(it))
# Raises StopIteration exception.  No 4th object to iterate
print('Iterate:', next(it))
