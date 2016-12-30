'''
Title    -  Writing Functions that Accepts any Number of Arguments   
Problem  -  Want to write a function that aceepts any number of input args  
'''

# * arguments
# any number of positional args 
# *rest is a tuple of all extr positional args passed
# codetreats as a seq for calcs 
# can only appear as last positional arg in function 
def avg(first, *rest):
  return (first + sum(rest)) / (1 + len(rest))
print('1:', avg(1,2))
print('2:', avg(1,2,3,4))

print('\n!---SECTION---\n')

# **keyword arguments 
# accepts any number of keyword args 
# attrs is a dictionary holds that passed keyword args
# can only appear as the last arg
import html 
def make_element(name, value, **attrs):
  keyvals = [' %s="%s"' % item for item in attrs.items()]
  attr_str = ''.join(keyvals)
  element = '<{name}{attrs}>{value}</{name}>'.format(
    name=name,
    attrs=attr_str,
    value=html.escape(value)
  )
  return element
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))

print('\n!---SECTION---\n')

# * & ** args
# function that can accept both any number of postional & key-word args 
def anyargs(*args, **kwargs):
  print('tuple:', args)   # tuple 
  print('dict:', kwargs) # dict
anyargs(1,2,3,4,5, a='a', b='b')

print('\n!---SECTION---\n')
  
# cannot have *args in the middle
# traceback
# def a(x, *args, y):
#  pass
# def b(x, *args, y, **kwargs):
#  pass

print('\n!---SECTION---\n')
