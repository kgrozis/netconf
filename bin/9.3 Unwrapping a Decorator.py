'''
Title    -  Unwrapping a Decorator  
Problem  -  Apply a decorator to a function 
            want to gain access to the orginial unwrapped function 
'''

# __wrapped__ attribute 
# gain access to the original function
from functools import wraps 
def somedecorator(func):
  print('somedecorator()')
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('wrapper()')
    result = func(*args, **kwargs)
    return result
  return wrapper 
@somedecorator
def add(x,y):
  return x+y 
print(add(3,4))
print('unwrap')
# direct access to unwrapped function 
# requires @wraps from functool to work 
orig_add = add.__wrapped__
print(orig_add(3,4))

print('\n!---SECTION---\n')

def decorator1(func):
  print('decorator1()')
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('decorator1.wrapper()')
    return func(*args, **kwargs)
  return wrapper 
def decorator2(func):
  print('decorator2()')
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('decorator2.wrapper()')
    return func(*args, **kwargs)
  return wrapper

@decorator1 
@decorator2
def add(x,y):
  print('add() ' + str(x + y))
add(2,3)
'unwrap '
add.__wrapped__(2,3)

print('\n!---SECTION---\n')

