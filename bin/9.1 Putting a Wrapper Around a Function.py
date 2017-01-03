'''
Title    -  Putting a Wrapper Around a Function  
Problem  -  Put a wrapper layer around a function that adds 
            extra processing (logging, timing, etc...) 
'''

# decorator function
# Need to wrap a function with extra code
# accepts functino as an input 
# returns a new function as output
import time 
from functools import wraps 
def timethis(func):
  '''
  Decorator that reports the execution time
  '''
  print('timethis()')
  @wraps(func)
  def wrapper(*args, **kwargs):
    # for flexibility assign *args, **kwargs so any func can be passed
    # wrapper executes additional code from passed func
    # wrapper won't alter execution or return of passed func 
    print('wrapper()')
    start = time.time()
    # execute function and save return 
    result = func(*args, **kwargs)
    end = time.time()
    print(func.__name__, end-start)
    # return passed function value
    return result
  return wrapper
@timethis 
# same as 
# countdown = timethis(countdown)
def countdown(n):
  '''
  Counts Down 
  '''
  print('countdown()')
  while n > 0:
    n-= 1
countdown(100000)
countdown(1000000)

print('\n!---SECTION---\n')

# built-in decorators
class A:
  @classmethod 
  def method(cls):
    pass 
class B: 
  # Equivalent of def of a class method 
  def method(cls):
    pass 
  method = classmethod(method)
