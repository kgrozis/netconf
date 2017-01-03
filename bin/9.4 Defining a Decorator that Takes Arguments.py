'''
Title    -  Defining a Decorator that Takes Arguments 
Problem  -  
'''

# logging 
# decorator adds logging to a function 
# user specifies the logging level & other args 
from functools import wraps 
import logging 

# outer function accepts args 
# makes args available to inner funcs of decorator
def logged(level, name=None, message=None):
  '''
  Add logging to a function. 
  level is the logging level,
  name is the logger name, 
  and message is the log message. 
  Defualt to a function's module & name. 
  '''
  print('logged()')

  # accepts functions
  # puts wrapper around it
  # wrapper use args passed to logged()
  def decorate(func):
    print('logged.decorate()')
    logname = name if name else func.__module__ 
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args,**kwargs):
      print('logged.decorate.wrapper()')
      log.log(level, logmsg)
      return func(*args, **kwargs)
    return wrapper 
  return decorate 

@logged(logging.DEBUG)
def add(x,y):
  print('add: {}'.format(x+y))
add(3,5)

@logged(logging.CRITICAL, 'example')
def spam():
  print('Spam!')
spam()

print('\n!---SECTION---\n')

'''

@decorator(x,y,z)
def func(a, b):
  pass 

Translates to:
def func(a, b):
  pass 
func = decorator(x,y,z)(func)
'''