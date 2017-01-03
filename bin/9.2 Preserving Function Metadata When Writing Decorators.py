'''
Title    -  Perserving Function Metadata When Writing Decorators  
Problem  -  Written a decorator
            Apply it to a function 
            Important metadata (name, string, annonation & signature) is lost
'''

# @wraps 
# functools library  
# keeps metadata - __name__, __doc__, __annotations__, etc...
import time 
from functools import wraps 
def timethis(func):
  print('timethis()')
  '''
  Decorator that reports the execution time. 
  '''
  # without @wraps metadata is from wrapper function
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('wrapper()')
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time() 
    print(func.__name__, end-start)
    return result 
  return wrapper
@timethis 
def countdown(n:int):
  '''
  Counts down 
  '''
  print('countdown()')
  while n > 0:
    n -= 1 
countdown(10000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

print('\n!---SECTION---\n')

# access wrapped function directly
print(countdown.__wrapped__(10000))

print('\n!---SECTION---\n')

# signature 
# expose underlying signature of the wrapped function 
from inspect import signature
print(signature(countdown))