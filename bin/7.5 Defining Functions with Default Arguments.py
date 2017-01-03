'''
Title    -  Defining Functions with Defualt Arguments  
Problem  -  Define a function where one or more of args are optional 
            & have a default value
'''

# Assign values in func def
# default args appear last
def spam(a,b=42):
  print('{} {}'.format(a,b)) 
spam(1)
spam(1,2)

print('\n!---SECTION---\n')

# if default value is mutable container 
# like list, set, or dict 
# use none as default 
def spam(a, b=None):
  if b is None:
    b =[]
  print('{} {}'.format(a,b)) 
spam(1)
spam(1,[2,3])

print('\n!---SECTION---\n')

# instead of default
# Want to test if arg was given an interesting value
_no_value = object()
def spam(a, b=_no_value):
  if b is _no_value:
    print('No b value supplied')
    b = ''
  print('{} {}'.format(a,b)) 
spam(1)
spam(1,2)
spam(1,None) # difference between no value & None

print('\n!---SECTION---\n')

# values assigned as a default are bound once at the time
#   of func def 
x = 42 
def spam(a, b=x):
  print('{} {}'.format(a,b)) 
spam(1)
x=23   # has no impact 
spam(1)

print('\n!---SECTION---\n')

# default values should be immutable
# such as None, True, False, numbers, or strings
# problems occur if value escapes function
# permanently alters the default value across future func calls 
def spam(a, b=[]):
  print(b)
  return b
x = spam(1)
print(x)
x.append(99)
x.append('Yow!')
print(x)
spam(1) # modified list is returned

print('\n!---SECTION---\n')

# best practice assign None as default
# create conditional check for None within func 
# critical to use 'is' operator in func 
def spam(a, b=None):
  if not b:
    b =[]
  print(b)
spam(1)       # OK
x = []
spam(1, x)    # Silent error.  x value overwritten
spam(1, 0)    # Silent error.  0 ignored
spam(1, '')   # Silent error.  '' ignored
print('---')
def spam(a, b=None):
  if b is None:
    b =[]
  print(b)
spam(1)
spam(1, x)    
spam(1, 0)    
spam(1, '')   
